from typing import List, Dict
from pathlib import Path
from sqlite3 import Cursor

from src.project.loading.loaderiterator import LoaderIterator
from src.project.transforming.batchtransformer import BatchTransformer
from src.project.transforming.currencyconverter import CurrencyConverter, latest_exchange_rates
from src.project.transforming.pricemultiplier import PriceMultiplier
from src.project.storing.sqlitecontextmanager import SQLiteContextManager
from src.project.storing.sqlitebatchproductstorer import SQLiteBatchProductStorer
from src.project.utils import accepts_types 
from src.project.utils import create_products



class DataPipeline:
    """A class that wraps the different components of the system. It processes
    data using these steps:  load -> apply transforms -> store
    """
    def __init__(self,
                 loader_iterator: LoaderIterator,
                 batch_transformer: BatchTransformer,
                 sqlite_context_manager: SQLiteContextManager,
                 storer: SQLiteBatchProductStorer) -> None:
        self.loader_iterator = loader_iterator
        self.batch_transformer = batch_transformer
        self.storer = storer
        self.sqlite_context_manager = sqlite_context_manager
    
    @accepts_types(list)
    def process(self, load_paths: List[Path]) -> None:
        """Process files in batches: load -> transform -> store to db."""
        self.loader_iterator.load_paths = load_paths
        with self.sqlite_context_manager as db_cursor:
            for product_data_batch in self.loader_iterator:
                self._process_product_batch(db_cursor, product_data_batch)
                             

    def _process_product_batch(self,
                               db_cursor: Cursor,
                               product_data_batch: List[Dict]) -> None:
        products = create_products(product_data_batch)
        transformed_products = self.batch_transformer.apply(products)
        self.storer.store(db_cursor, transformed_products)
        
def create_hardcoded_data_pipeline() -> DataPipeline:
    ### TODO create arguments for direct injection
    loader_iterator = LoaderIterator(JsonSerializer(), 2)
    batch_transformer = BatchTransformer(
         [CurrencyConverter(latest_exchange_rates, "euro"),
         PriceMultiplier(0.8)])
    product_storer = SQLiteBatchProductStorer()
    sqlite_context_manager = SQLiteContextManager("test.db")
    return DataPipeline(loader_iterator,
                        batch_transformer,
                        product_storer,
                        sqlite_context_manager)                                     
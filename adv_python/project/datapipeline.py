from typing import List, Dict
from pathlib import Path
import sqlite3

from transforming.batchtransformer import BatchTransformer
from transforming.currencyconverter import CurrencyConverter, latest_exchange_rates
from transforming.pricemultiplier import PriceMultiplier
from storing.sqlitecontextmanager import SQLiteContextManager
from storing.sqlitebatchproductstorer import SQLiteBatchProductStorer
from storing.createdb import create_db
from loading.loaderiterator import LoaderIterator
from loading.serialization import JsonSerializer
from utils import accepts_types, create_products, create_file_paths_from_dir 



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
                               db_cursor: sqlite3.Cursor,
                               product_data_batch: List[Dict]) -> None:
        products = create_products(product_data_batch)
        transformed_products = self.batch_transformer.apply(products)
        self.storer.store(db_cursor, transformed_products)
        
def create_hardcoded_data_pipeline() -> DataPipeline:
    ### TODO create arguments for direct injection
    loader_iterator = LoaderIterator(JsonSerializer(), 2, None)
    batch_transformer = BatchTransformer(
         [CurrencyConverter(latest_exchange_rates, "euro"),
         PriceMultiplier(0.8)])
    product_storer = SQLiteBatchProductStorer()
    sqlite_context_manager = SQLiteContextManager("/home/jbjoyce/soundofaiacademy/adv_python/project/test.db")
    return DataPipeline(loader_iterator,
                        batch_transformer,
                        sqlite_context_manager,
                        product_storer,)
    

                                      
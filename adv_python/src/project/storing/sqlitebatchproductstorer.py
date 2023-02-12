from typing import List, Tuple

import sqlite3

from src.project.product import Product
from src.project.utils import accepts_types




class SQLiteBatchProductStorer:
    """This class is responsible for batch inserting products into the db"""
    
    def __init__(self, table: str = "product") -> None:
        self.table = table
        
    @accepts_types(sqlite3.Cursor, list)
    def store(self, 
              db_cursor: sqlite3.Cursor,
              products: List[Product]) -> None:
        """Batch insert list of products in the 'product' table of the db."""
        products_list = self._convert_products_to_list_of_tuples(products)
        db_cursor.executemany(f"INSERT INTO {self.table}(name, currency, price) VALUES(?, ?, ?)", products_list)
        
    @staticmethod
    def _convert_products_to_list_of_tuples(products: List[Product]) -> List[Tuple[str, str, float]]:
        return [product.to_tuple() for product in products]
    
               
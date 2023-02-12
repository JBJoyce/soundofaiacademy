"""This is a simple script to generate a dummy sqlite database with single
table called 'products'.
"""

from sqlite3 import connect



def create_db(db_path: str) -> None:
    """Create an sqlite db with a single table called 'product'"""
    connection = connect(db_path)
    print(f"Create database successfully and stored at '{db_path}'")
    connection.execute(
        '''
        CREATE TABLE PRODUCT
        (ID INTEGER    PRIMARY KEY      AUTOINCREMENT,
        NAME           CHAR(50)         NOT NULL,
        CURRENCY       CHAR(20)         NOT NULL,
        PRICE          REAL             NOT NULL)
        '''    
    )
    print("'Product' table create successfully")
    
if __name__ == "__main__":
    create_db("/home/jbjoyce/soundofaiacademy/adv_python/project/storing/product.db")
        
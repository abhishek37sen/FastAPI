# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()



import sqlite3


class DataBase:
    def __init__(self):
        self.create_connection()
        self.create_tabel()

    def create_connection(self):
        self.conn = sqlite3.connect("app.db")
        self.curr = self.conn.cursor()

    def create_tabel(self):
        self.curr.execute(''' Drop table if exists product''')
        self.curr.execute(''' create table product(
                                product_name text,
                                price number )''')

    def insert_data(self,product_name,price):
        self.curr.execute('INSERT INTO product VALUES (?,?)',(product_name,price))
        self.conn.commit()
db = DataBase()
db.create_tabel()
db.insert_data('skoda',50000)
db.insert_data('swift',70000)
db.insert_data('innova',100000)
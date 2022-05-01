
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from flask_sqlalchemy import SQLAlchemy


SQLITE = 'sqlite'

# Table Names
BOOKS = 'Books'
CUSTOMERS = 'Customers'
LOANS = "Loans"


class MyDatabase:

    DB_ENGINE = {
         SQLITE: 'sqlite:///{DB}'

    }

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)

            self.db_engine = create_engine(engine_url)
            print(self.db_engine)

        else:
            print("DBType is not found in DB_ENGINE")


    # create tables
    def create_db_tables(self):
        metadata = MetaData()
        books = Table(BOOKS, metadata,
                      Column('bookID', Integer, primary_key=True),
                      Column('name', String),
                      Column('author', String),
                      Column('year_published', String),
                      Column('book_type', Integer)
                      )

        cutomers = Table(CUSTOMERS, metadata,
                         Column('custID', Integer, primary_key=True),
                         Column('email', String),
                         Column('password', String),
                         Column('name', String),
                         Column('city', String),
                         Column('age', Integer)
                         )
        loans = Table(LOANS, metadata,
                      Column('custID', Integer),
                      Column('bookID', Integer),
                      Column('loandate', String),
                      Column('returndate', String)
                      )

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    # Insert, Update, Delete
    def execute_query(self, query=''):
        if query == '':
            return

        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    # print all data from tables
    def print_all_data(self, table='', query=''):
        query = query if query != '' else f"SELECT * FROM {table}"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append(row)
                    # print(row) # print(row[0], row[1], row[2])
                result.close()
        # print("\n")
        return res

    # Delete by var of choise
    def delete_by_(self, table, someID,id):
        
        
        query = f"DELETE FROM {table} WHERE {someID}={id}"
        self.execute_query(query)

    # inserts
    def insert_new_customer(self, name, email, password, city, age):
        query = f"INSERT INTO {CUSTOMERS}(name,email,password, city,age) VALUES('{name}','{email}','{password}','{city}',{age})"
        self.execute_query(query)

    def insert_new_book(self, name, author, year_published, book_type):
        query = f"INSERT INTO {BOOKS}( name, author,year_published,book_type) VALUES('{name}','{author}','{year_published}',{book_type});"
        self.execute_query(query)

    def loan(self, custID, bookID, loandate, returndate):
        query = f"INSERT INTO {LOANS}(custID ,bookID,loandate,returndate) VALUES({custID},{bookID},'{loandate}','{returndate}')"
        self.execute_query(query)
    

    # check if loo
    def check_log(self,email,password):
        query = f"SELECT password FROM customers WHERE email = '{email}'  and password = '{password}'"
        self.execute_query(query=query)
        return self.print_all_data(query=query)
        
        


    # get data by _
    def get_by_somthing(self,wht,tab,frm,lke):
        
        query = f"SELECT {wht} FROM {tab} WHERE {frm} = '{lke}';"
        self.execute_query(query=query)
        return self.print_all_data(query=query)

    def get_by_int(self,wht,tab,frm,lke):
        
        query = f"SELECT {wht} FROM {tab} WHERE '{frm}' = {lke};"
        self.execute_query(query)
        return self.print_all_data(query)
    # update
    def update(self,tbl,set,eq0,where,eq1):
            # query = f"UPDATE {} set first_name='XXXX' WHERE id={id}"\.format(BOOKS, id=3)
                
            query = f"UPDATE {tbl} set {set}='{eq0}' WHERE {where}='{eq1}'" 
            self.execute_query(query)    



  
        
        

Library Manegment App
Author > Leon Sher
Date > 15/4/2022
Github > https://github.com/leonkingsher/lolib
Heroku > https://lolibar.herokuapp.com/
demo admin > email: admin@lolib.com  password: 12345
__________________________________
Frontend >  html/css (Bootstrap) 
Backend > - Python flask (pip install flask)
Database > sqlite - sqlalchemy DAL (pip install sqlalchemy)
__________________________________
App summary: Simple, user freandly, library Manegment app.
The user can log-in and sing-up, insert new book into the library colection, loan a book and return it eventualy, user can also add a new customer, delete an exsiting one.


                                  DATABASE (DAL)
__________________________________________________________________________________ 

database/madatabase.py  module >> 'MyDatabase' class > uses 'sqlalchemy' pack to establish the connection, create the DB tables and hold all the DB modification functions;

    def create_db_tables(self)
    def execute_query(self, query='')
    def print_all_data(self, table='', query='')
    def delete_by_(self, table, id)
    def insert_new_customer(self, name, email, password, city, age)
    def insert_new_book(self, name, author, year_published, book_type)
    def loan(self, custID, bookID, loandate, returndate)
    def check_log(self,email,password)
    def get_by_somthing(self,wht,tab,frm,lke)
    def get_by_int(self,wht,tab,frm,lke)
    def update(self,tbl,set,eq0,where,eq1)


                                    FLASK MODULS AND BLUEPRINTS
__________________________________________________________________________________ 
main.py - main app module

main.py (main app) >> 'home()' func > routhe('/') > rendering 'home.html' - no actions 
__________________________________________________________________________________ 

books.py (blueprint) >> add_new_book() func > route('/new_book') > rendering 'add_new_book.html' > uses 'insert_new_book' method from 'mydatabase.py'(DAL) - adding a new book

books.py (blueprint) >> loan() func > route('/loans/<>') > rendering 'display_books.html' > uses 'loan' method from 'mydatabase.py'(DAL) - adding a new loan 

books.py (blueprint) >> return_a_book() func > route('/return/<>') > rendering 'display_books.html' > uses 'update' method from 'mydatabase.py'(DAL) - updating the return date 

__________________________________________________________________________________ 

display.py (blueprint) >> display_books() func > route('/books') > rendering 'display_books.html' > uses 'print_all_data' method from 'mydatabase.py'(DAL) - display all the books 

display.py (blueprint) >> display_customers() func > route('/customers') > rendering 'display_customers.html' > uses 'print_all_data' method from 'mydatabase.py'(DAL) - display all the customers 

display.py (blueprint) >> display_loans() func > route('/loans') > rendering 'display_loans.html' > uses 'print_all_data' method from 'mydatabase.py'(DAL) - display all active loans & shows if the return date is over 

display.py (blueprint) >> book_by_name() func > route('/book_by_name') > rendering 'find_book.html' > uses 'get_by_somthing' method from 'mydatabase.py'(DAL) - display searched book 


__________________________________________________________________________________ 

customers.py (blueprint) >> add_new_customer() func > route('/singup') > rendering 'singup.html' > uses 'insert_new_customer' method from 'mydatabase.py'(DAL) - checks if a customer exists by an email, if not add new customer to the CUSTOMERS table
 
 customers.py (blueprint) >> login() func > route('/login') > rendering 'log.html' > uses 'check_log' method from 'mydatabase.py'(DAL) to check the credentials  - saves in a session the logging credentials

 customers.py (blueprint) >> find_customer() func > route('/find') > rendering 'find_cust.html' > uses 'get_by_somthing' method from 'mydatabase.py'(DAL) - display searched Customer

 customers.py (blueprint) >> logout() func > route('/logout') > renderects to 'customers.login()' > uses session.clear() method to empty the session 

 __________________________________________________________________________________ 

halper.py (blueprint) >> del_by_cust() func > route('/delcustomer<>') > redirecting ('/display/customers') > uses 'delete_by_' method from 'mydatabase.py'(DAL) - delets the chosen customer

halper.py (blueprint) >> del_by_book() func > route('/delbook<>') > redirecting ('/display/books') > uses 'delete_by_' method from 'mydatabase.py'(DAL) - delets the chosen book
 


                                    HTML TEMPLATES & OTHER FILES
__________________________________________________________________________________ 

templates/ > all the .html pages used as a frontend

layout.html >> main tamplate used by other > main nav-bar and Bootstrap files

static/ > pictures used 

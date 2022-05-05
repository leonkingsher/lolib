# Library Manegment App
# Tech used >  Python flask - html/css (Bootstrap) - SQL (sqlalchemy)
# Author > Leon Sher
# Date > 15/4/2022
# Github > https://github.com/leonkingsher/lolib


from flask import Flask,render_template,redirect,url_for,session,flash,request,Blueprint
from app import mydatabase
from app.customers import customers
from app.display import display
from app.books import books
from app.helper import helper

dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='library.sqlite')
app = Flask(__name__)
app.secret_key = "111"

dbms.create_db_tables()

app.register_blueprint(customers)
app.register_blueprint(display)
app.register_blueprint(books)
app.register_blueprint(helper)


@app.route('/')
def home():
        return render_template('home.html')

# if __name__ == "__main__":
#     app.run(debug=True)    

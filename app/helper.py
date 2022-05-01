
from flask import Blueprint, Flask,render_template,redirect,url_for,session,flash,request
from app import mydatabase

helper = Blueprint('helper',__name__, url_prefix='/helper')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='library.sqlite')






@helper.route('/delcustomer/<i>')
def del_by_cust(i):
    print(i)
    dbms.delete_by_(mydatabase.CUSTOMERS,'custID',i)
    return redirect('/display/customers')


@helper.route('/delbook/<i>')  
def del_by_book(i):
    print(i)
    dbms.delete_by_(mydatabase.BOOKS,'BookID',i)
    return redirect('/display/books')



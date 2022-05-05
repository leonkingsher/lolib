
from flask import Blueprint, Flask,render_template,redirect,url_for,session,flash,request
from app.customers import customers
from app import mydatabase
from datetime import date


books = Blueprint('books',__name__, url_prefix='/books')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='library.sqlite')

books.register_blueprint(customers)


@books.route('/new_book', methods = ['POST','GET'])
def add_new_book():
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        year_published = request.form['year_published']
        type = request.form['type']
        dbms.insert_new_book(name,author,year_published,type)

        return redirect(url_for('books.add_new_book'))
    return render_template('add_new_book.html')    


@books.route('/loans/<i>')
def loan(i):
    try:
        
        bid=dbms.get_by_somthing('custID',mydatabase.CUSTOMERS,'email',session['email'])
        for e in bid:
            b = str(e).strip('(').strip(')').strip(',')
        custID = b
        bookID = str(i).strip("'")
        loandate = date.today()
        returndate ='Not Yet'
        check_if_taken= dbms.get_by_somthing('bookID',mydatabase.LOANS,'bookID',bookID)
        if check_if_taken ==[]:
            dbms.loan(custID,bookID,loandate,returndate)
            print('loan seccess')
        return redirect(url_for('display.display_books',))
    except Exception as e:
        print(e)    

        return render_template('display_books.html')


@books.route('/return/<i>')
def return_a_book(i):
    today_date = date.today()
    dbms.update(mydatabase.LOANS,'returndate',today_date,"bookID",i )
    flash('success')
    return redirect('/')


# /books/return/{{i[2]}}    
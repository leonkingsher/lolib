
from flask import Blueprint, Flask,render_template,redirect,url_for,session,flash,request
from app import mydatabase
from datetime import date, datetime

display = Blueprint('display',__name__, url_prefix='/display')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='library.sqlite')




# dislpay functions
@display.route('/books')
def display_books():
    res = dbms.print_all_data(mydatabase.BOOKS)
    if res ==[]:flash('No results')
    return render_template('display_books.html',res=res)

@display.route('/customers')
def display_customers():
    res = dbms.print_all_data(mydatabase.CUSTOMERS)
    if res ==[]:flash('No results')
    return render_template('display_customers.html',res=res)




@display.route('/book_by_name', methods=["POST",'GET'])
def book_by_name():
    if request.method == "POST":
        data = request.form['search']
        res = dbms.get_by_somthing('*',mydatabase.BOOKS,'name',data)
        print(res)
        if res ==[]:flash('No results')
        return render_template('find_book.html',res=res)
    
    return render_template('find_book.html')


@display.route('/loans')
def display_loans():
    type1 = 10
    type2 = 5
    type3 = 2
    loan_date_lst = []
    all_loans = dbms.print_all_data( query='select name,book_type,loans.* from Books inner join loans on books.bookID = loans.bookID and loans.returndate ="Not Yet"')
    for loan in all_loans:
        print(loan)
        splited_date = loan[-2].split('-')
        y = int(splited_date[0])
        m = int(splited_date[1])
        d = int(splited_date[2])
        loan_date_fin = date(y,m,d)
        today_date = date.today()
        loan_days = (today_date-loan_date_fin).days
        book_type = loan[1]



        if int(book_type) == 1 and type1 < loan_days:
                loan_date_lst.append(f'{type1 - loan_days} days late')
                fraze = f'{type1 - loan_days} days late'
        elif int(book_type) == 2 and type2 < loan_days:
                loan_date_lst.append(f'{type2 - loan_days} days late')
                
        elif int(book_type) == 3 and type3 < loan_days:
                loan_date_lst.append(f'{type3 - loan_days} days late')
            #     
        else: loan_date_lst.append('Enjoy your book, You have few days left')
        
        
    return render_template('display_loans.html',context={'loans':all_loans,'iflate':loan_date_lst})
            
            

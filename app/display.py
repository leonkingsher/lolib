
from flask import Blueprint, Flask,render_template,redirect,url_for,session,flash,request
from app import mydatabase
from datetime import date

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

@display.route('/loans')
def display_loans():
    res = dbms.print_all_data(mydatabase.LOANS)
    if res ==[]:flash('No results')
    return render_template('display_loans.html',res=res)


@display.route('/book_by_name', methods=["POST",'GET'])
def book_by_name():
    if request.method == "POST":
        data = request.form['search']
        res = dbms.get_by_somthing('*',mydatabase.BOOKS,'name',data)
        print(res)
        if res ==[]:flash('No results')
        return render_template('find_book.html',res=res)
    
    return render_template('find_book.html')


@display.route('/late_loans')
def display_late_loans():
    all_loans = dbms.print_all_data(mydatabase.LOANS)

    type1 = 10
    type2 = 5
    type3 = 2
    
    try:
        # booktype
        loaned_book_type = dbms.print_all_data( query='select "book_type" from Books inner join loans on books.bookID = loans.bookID and loans.returndate ="Not Yet"')
        for book in loaned_book_type:
            book_type  = str(book).strip('(').strip(')').strip(',')

        # loan_days
        loan_date = dbms.print_all_data( query='select "loandate" from loans  inner join Books on books.bookID = loans.bookID and loans.returndate ="Not Yet"')
        for dat in loan_date:
            date_str  = str(dat).strip('(').strip(')').strip(',').strip("'")
            splited_date = date_str.split('-')
            y = int(splited_date[0])
            m = int(splited_date[1])
            d = int(splited_date[2])
            loan_date_fin = date(y,m,d)
            today_date = date.today()
            loan_days = (today_date-loan_date_fin).days
            


        if int(book_type) == 1:
            if type1 < loan_days:
                print(f'book_type1 = {book_type}')
                context = {"all_loans":all_loans, "late":f'{type1 - loan_days} days late'  }
                return render_template("late_loans.html",context= context)

        if int(book_type) == 2:
            if type2 < loan_days:
                context = {"all_loans":all_loans, "late":f'{type2 - loan_days} days late'  }
                
                return render_template("late_loans.html",context = context)       
        if int(book_type) == 3:
            if type3 < loan_days:
                context = {"all_loans":all_loans, "late":f'{type3 - loan_days} days late'  }
                return render_template("late_loans.html",context= context)
        else:
            flash('No results')
            context = {"all_loans":all_loans, "late":'None'  }
            return render_template("late_loans.html",context= context)

    except Exception as e:
        print(e)
        flash('No results')
        return render_template("late_loans.html",context= {"all_loans":all_loans, "late":'None'  })     

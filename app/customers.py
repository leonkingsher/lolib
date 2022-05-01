from flask import Blueprint, Flask,render_template,redirect,url_for,session,flash,request

from app import mydatabase

customers = Blueprint('customers',__name__, url_prefix='/customers')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='library.sqlite')




# sing up
@customers.route('/signup', methods = ['POST','GET'])
def add_new_customer():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        city = request.form['city']
        age = request.form['age']
        es = dbms.get_by_somthing('email',mydatabase.CUSTOMERS,'email',email)
        print(es)
        if es == []:
            dbms.insert_new_customer(name,email,password,city,age)
            return redirect(url_for('customers.login'))
        else: flash('Customer with this email already exists')
              
    return render_template('signup.html')  


# log in
@customers.route("/login", methods = ['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        check = dbms.check_log(email,password)

        print(f'the result is {check}')
        if check != [] :
            session['email'] = email
            session['password'] = password
            print(session)
            name = dbms.get_by_somthing('name',mydatabase.CUSTOMERS,'email',email)
            for nam in name:
                na = str(nam).strip('(').strip(')').strip("'").strip(',').strip("'")
            # flash(f'Hello, {na} Logged in successfully!','info')
            session['name'] = na
            return redirect(url_for('home'))

        else: 
            flash('Invalid credentials!','info')
            return render_template('log.html')       
    else:
        return render_template('log.html')    


# find customer by name
@customers.route('/find', methods=["POST",'GET'])
def find_customer():
    if session['email'] =='admin@lolib.com':
        if request.method == "POST":
            data = request.form['search']
            res = dbms.get_by_somthing('*',mydatabase.CUSTOMERS,'name',data)
            if res ==[]:flash('No results')
            return render_template('find_cust.html',res=res)
        return render_template('find_cust.html')
    else: return redirect(url_for('customers.login'))

# log out
@customers.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect(url_for('customers.login'))
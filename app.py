'''from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def sql_connector():
    conn = mysql.connector.connect(user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()
    return conn, cursor

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            username = request.form['name']
            email = request.form['email']
            password = request.form['password1']
            phone = request.form['phno']

            conn, cursor = sql_connector()
            query = "INSERT INTO leo (username, email, password, phone) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, email, password, phone))

            conn.commit()
            conn.close()
            cursor.close()

            flash('Data stored successfully!', 'success')
            print(username, email, password)

        except mysql.connector.Error as error:
            flash('An error occurred while storing the data!', 'error')
            print('Error:', error)

    return render_template("login.html")

@app.route('/app.py', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email2 = request.form['name2']
        password2 = request.form['password2']
        if password2 is None or password2 == "":
            return redirect(url_for("nit", name="Invalid Password!"))

        connection = mysql.connector.connect(host='localhost', user='root', password='prem@2003', database='mclovin')
        cursor = connection.cursor()

        # Execute a SELECT query to check if the provided username and password match a record in the database
        query = "SELECT * FROM leo WHERE email = %s AND password = %s"
        cursor.execute(query, (email2, password2))

        result = cursor.fetchone()

        # Close the cursor and the database connection
        cursor.close()
        connection.close()

        if result:
            # Redirect to the index.html page if login is successful
            return redirect(url_for("index"))
        else:
            # Redirect back to the login page with an error message if login fails
            return redirect(url_for("nit", name="Invalid Login!"))

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/<name>")
def nit(name):
    return render_template("login.html", content=name)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')
@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

if __name__ == "__main__":
    app.run(debug=True)'''






from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def sql_connector():
    conn = mysql.connector.connect(user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()
    return conn, cursor

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            username = request.form['name']
            email = request.form['email']
            password = request.form['password1']
            phone = request.form['phno']

            conn, cursor = sql_connector()
            query = "INSERT INTO leo (username, email, password, phone) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, email, password, phone))

            conn.commit()
            conn.close()
            cursor.close()

            flash('Data stored successfully!', 'success')
            print(username, email, password)

        except mysql.connector.Error as error:
            flash('An error occurred while storing the data!', 'error')
            print('Error:', error)

    return render_template("login.html")

@app.route('/app.py', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email2 = request.form['name2']
        password2 = request.form['password2']
        if password2 is None or password2 == "":
            return redirect(url_for("nit", name="Invalid Password!"))

        connection = mysql.connector.connect(host='localhost', user='root', password='prem@2003', database='mclovin')
        cursor = connection.cursor()
        

        # Execute a SELECT query to check if the provided username and password match a record in the database
        query = "SELECT * FROM leo WHERE email = %s AND password = %s"
        cursor.execute(query, (email2, password2))

        result = cursor.fetchone()

        # Close the cursor and the database connection
        cursor.close()
        connection.close()

        if result:
            # Redirect to the index.html page if login is successful
            return redirect(url_for("index"))
        else:
            # Redirect back to the login page with an error message if login fails
            return redirect(url_for("nit", name="Invalid Login!"))

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/<name>")
def nit(name):
    return render_template("login.html", content=name)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


@app.route('/services', methods=['GET', 'POST'])
def services():
    if request.method == 'POST':
        try:
            name = request.form['name3']
            email = request.form['email3']
            phno = request.form['phno3']
            services = request.form['Service']
            time = request.form['time']
            description = request.form['description']

            conn, cursor = sql_connector()
            query = "INSERT INTO service (name, email, phno, services, time, description) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (name, email, phno, services, time, description))

            conn.commit()
            cursor.close()
            conn.close()

            flash('Data stored successfully!', 'success')
            print(query, (name, email, phno, services, time, description))

            return redirect(url_for('services'))  # Redirect to the services page after successful form submission

        except mysql.connector.Error as error:
            flash('An error occurred while storing the data!', 'error')
            print('Error:', error)

    return render_template('services.html')
@app.route('/inner')
def table_data():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn =  mysql.connector.connect(
        user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "select * from leo INNER JOIN service ON leo.email=service.email;"
    cursor.execute(query)
    table_data = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with table data as response
    return render_template('inner.html', table_data=table_data)
    # return render_template('index.html')


@app.route('/left')
def table():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn =  mysql.connector.connect(
        user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "select * from leo LEFT JOIN service ON leo.email=service.email;"
    cursor.execute(query)
    table = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with table data as response
    return render_template('left.html', table=table)
    # return render_template('index.html')

@app.route('/operation')
def operation():
    return render_template('button.html')


@app.route('/right')
def right():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn =  mysql.connector.connect(
        user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "select * from leo RIGHT JOIN service ON leo.email=service.email;"
    cursor.execute(query)
    right = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with right data as response
    return render_template('right.html', right=right)
    # return render_template('index.html')
@app.route('/full')
def full():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn =  mysql.connector.connect(
        user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "select * from leo LEFT JOIN service ON leo.email=service.email;"
    cursor.execute(query)
    full = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with full data as response
    return render_template('full.html', full=full)
    # return render_template('index.html')
@app.route('/union')
def union():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn =  mysql.connector.connect(
        user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "SELECT username, email FROM leo WHERE username='Rakesh' UNION SELECT name, email FROM service WHERE name='prem' ORDER BY username;"
    cursor.execute(query)
    union = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with union data as response
    return render_template('union.html', union=union)
    # return render_template('index.html')

@app.route('/ino')
def ino():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn =  mysql.connector.connect(
        user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "SELECT * FROM leo WHERE username IN ('Rakesh','prem');"
    cursor.execute(query)
    ino = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with ino data as response
    return render_template('in.html', ino=ino)
    # return render_template('index.html')


@app.route('/between')
def between():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn =  mysql.connector.connect(
        user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "SELECT * FROM service WHERE name BETWEEN 'prem' AND 'Rakesh' ORDER BY name;"
    cursor.execute(query)
    between = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with between data as response
    return render_template('between.html', between=between)
    # return render_template('index.html')
@app.route('/dis')
def dis():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn =  mysql.connector.connect(
        user='root', password='prem@2003', db='mclovin', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "SELECT DISTINCT username FROM leo;"
    cursor.execute(query)
    dis = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with dis data as response
    return render_template('distinct.html', dis=dis)
    # return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)


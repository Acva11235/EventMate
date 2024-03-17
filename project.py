from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
import jinja2

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysql1234'
app.config['MYSQL_DB'] = 'eventmate'

mysql = MySQL(app)

@app.route('/home', methods=['GET', 'POST'])
def home():

    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)





































# @app.route('/home', methods=['GET', 'POST'])
# def home():

#     return render_template("landing_page_donor.html")


# @app.route('/login-link', methods=['GET', 'POST'])
# def login_link():
#     return render_template("ngo_donor_login_link.html")


# @app.route('/signup-donor', methods=['GET', 'POST'])
# def signup_donor():

#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         pswd = request.form.get('password')
#         contact = request.form.get('contact')
#         address = request.form.get('address')
#         # conn= mysql.connector.connect(host="localhost", user="root", password= "Mysql1234",database="sharemeals")
#         # cur=conn.cursor()
#         cur = mysql.connection.cursor()
#         cur.execute("insert into donor values('%s','%s','%s','%s','%s')" % (username, address, contact, email, pswd))
#         mysql.connection.commit()

#         return render_template("donor_login.html")

#     return render_template("donor_sign_up.html")


# @app.route('/login-donor', methods=['GET', 'POST'])
# def login_donor():
#     if request.method == 'POST':
#         cur = mysql.connection.cursor()
#         user = request.form.get('username')
#         password = request.form.get('password')
#         cur.execute("select * from donor where name = '%s';"%(user))
#         data = cur.fetchone()
#         print(data)

#         if data == None:
#             return render_template('ngo_donor_login_link.html')


#         elif password == data[-1]:
#             print("valid successfully")
#             return render_template("landing_page_donor.html")

#         else:
#             return render_template('ngo_donor_login_link.html')

#         # print(user)
#         # print(password)

#     return render_template('donor_login.html')


# @app.route('/login-ngo', methods=['GET', 'POST'])
# def login_ngo():
#     if request.method == 'POST':
#         cur = mysql.connection.cursor()
#         user = request.form.get('username')
#         password = request.form.get('password')
#         cur.execute("select * from ngo where name = '%s';"%(user))
#         data = cur.fetchone()

#         if data == None:
#             return render_template('ngo_donor_login_link.html')

#         elif password == data[-1]:
#             print("valid successfully")
#             return render_template("landing_page_ngo.html")

#         else:
#             return render_template('ngo_donor_login_link.html')

#         # print(user)
#         # print(password)

#     return render_template('ngo_login.html')


# @app.route('/signup-ngo', methods=['GET', 'POST'])
# def signup_ngo():
#     if request.method == 'POST':
#         cur = mysql.connection.cursor()
#         name = request.form.get('ngoname')
#         email = request.form.get('email')
#         pswd = request.form.get('password')
#         contact = request.form.get('contact')
#         about = request.form.get('about')
#         tagline = request.form.get('tagline')
#         # conn= mysql.connector.connect(host="localhost", user="root", password= "Mysql1234",database="sharemeals")
#         # cur=conn.cursor()
#         cur = mysql.connection.cursor()
#         cur.execute( "insert into ngo values('%s','img','%s','%s','0','0','yes','%s','%s','%s');"% (name, about, tagline, contact, email,pswd))
#         mysql.connection.commit()




#     return render_template("ngo_signup.html")

# @app.route('/donate', methods=['GET', 'POST'])
# def donate():
#     cur = mysql.connection.cursor()
#     cur.execute("select * from ngo where reqchk='yes';")
#     ngolist = cur.fetchall()


#     return render_template("ngo_list.html", ngolist=ngolist)


# @app.route('/collect', methods=['GET', 'POST'])
# def collect():
#     cur = mysql.connection.cursor()
#     cur.execute("select * from donations;")
#     donorlist = cur.fetchall()

#     return render_template("donor_list.html",donorlist=donorlist)


# @app.route('/home-ngo', methods=['GET', 'POST'])
# def home_ngo():

#     return render_template("landing_page_ngo.html")


# if __name__ == "__main__":
#     app.run(debug=True)
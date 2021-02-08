from flask import Flask
from flask_mysql_connector import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Amroha@123#'
app.config['MYSQL_DB'] = 'DEMO'



@app.route('/', methods=['GET', 'POST'])
def home():
    cur = mysql.new_cursor(dictionary=True)
    # give database name inside sql query
    EXAMPLE_SQL = 'SELECT * FROM DEMO.MyUsers'
    cur.execute(EXAMPLE_SQL)
    output = cur.fetchall()
    print(output)
    return "hello", str(output)


if __name__=='__main__':
    app.run()


from flask import Flask,request,render_template,url_for,redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="yout user name",
    passwd="your password",
    database="database name"
)
cursor = db.cursor()

@app.route('/',methods=['GET','POST'])
def hello_world():
    login =""
    data = request.form
    email = data.get("email")
    password = data.get("password")
    print(email)
    print(password)

    if(email and password):
        try:
            q = f'SELECT * FROM login_form WHERE email="{email}" and password="{password}"'
            print(q)
            result = cursor.execute(q)
            result = cursor.fetchall()
            if result:
                print("database exits")
                return redirect(url_for("success"))
            else:
                login = "Error Login"
                print("database does not exist")

        except Exception as e:
            print(f"Something went wrong {e}")
    return render_template("index.html",login=login)


@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)

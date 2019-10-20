from flask import Flask, render_template, request
import sqlite3

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result", methods=["GET"])
def result():
    subject = request.form.get("waste")
    data = getDirt(subject)

    return render_template("result.html",name=data[0],waste=data[1],recyclable=data[2],procedure=data[3])

def getDirt(info):
    conn = sqlite3.connect('TestDB.db') 
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE name='"+info+"'")
    a = c.fetchall()
    print(a)
    return a





# run the application
if __name__ == "__main__":
    app.run(debug=True)

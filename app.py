from flask import Flask, render_template, request
import sqlite3

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user/")
def user():
    return render_template('user.html')


@app.route("/dry/")
def dry():
    return render_template('dry.html')


@app.route("/wet/")
def wet():
    return render_template('wet.html')


@app.route("/waste", methods=["POST"])
def result():
    subject = request.form.get("topic")
    data = getDirt(subject)
    print(data)
    return render_template("waste.html", name=data[0], waste=data[1], recyclable=data[2], procedure=data[3], image1=data[4], image2=data[5], image3=data[6])


def getDirt(info):
    conn = sqlite3.connect('TestDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE name='"+info+"'")
    a = c.fetchall()
    print(a)
    return a[0]


# run the application
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import render_template

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


# run the application
if __name__ == "__main__":
    app.run(debug=True)

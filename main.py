from flask import Flask, render_template, request

# create an instance of flask object
app = Flask(__name__)


# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")


@app.route("/allie")
def allie():
    return render_template("allie.html")


@app.route("/gabriel")
def gabriel():
    return render_template("gabriel.html")


@app.route("/justin")
def justin():
    return render_template("justin.html")


@app.route("/rebecca")
def rebecca():
    return render_template("rebecca.html")


@app.route("/tianbin")
def tianbin():
    return render_template("tianbin.html")


if __name__ == "__main__":
    app.run(debug=True)

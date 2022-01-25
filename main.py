import requests
from flask import render_template
from __init__ import app
from crud.app_crud import app_crud
from crud.app_crud_api import app_crud_api

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)


# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")


@app.route("/about-the-exam")
def about_the_exam():
    return render_template("about_the_exam.html")


@app.route("/allie")
def allie():
    return render_template("about_us/allie.html")


@app.route("/gabriel")
def gabriel():
    return render_template("about_us/gabriel.html")


@app.route("/justin")
def justin():
    return render_template("about_us/justin.html")


@app.route("/tianbin")
def tianbin():
    return render_template("about_us/tianbin.html")


@app.route("/gabeMinigame")
def gabeMinigame():
    return render_template("about_us/gabeMinigame.html")


@app.route("/rebecca", methods=["GET", "POST"])
def rebecca():
    url = "https://free-nba.p.rapidapi.com/teams"

    querystring = {"page": "0"}

    headers = {
        'x-rapidapi-host': "free-nba.p.rapidapi.com",
        'x-rapidapi-key': "199e385baamshc0a4c645191a179p191ebdjsn70f0155c5394"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return render_template("about_us/rebecca.html", data=data)


@app.route("/collaboration")
def collaboration():
    return render_template("Big Ideas/Big Idea 1/collaboration.html")


@app.route("/program-design")
def program_design():
    return render_template("Big Ideas/Big Idea 1/program_design.html")


@app.route("/program-function")
def program_function():
    return render_template("Big Ideas/Big Idea 1/program_function.html")


@app.route("/identifying-and-correcting-errors")
def errors():
    return render_template("Big Ideas/Big Idea 1/errors.html")


@app.route("/support")
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)

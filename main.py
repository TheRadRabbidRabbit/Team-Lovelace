import requests
from flask import Flask, render_template

# create an instance of flask object
app = Flask(__name__)


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
    return render_template("allie.html")


@app.route("/gabriel")
def gabriel():
    return render_template("gabriel.html")


@app.route("/justin")
def justin():
    return render_template("justin.html")


@app.route("/tianbin")
def tianbin():
    return render_template("tianbin.html")


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
    return render_template("rebecca.html", data=data)


@app.route("/collaboration")
def collaboration():
    return render_template("Big Idea/Big Idea 1/collaboration.html")


@app.route("/creative-development")
def creative_development():
    return render_template("Big Idea/Big Idea 1/creative_development.html")


@app.route("/program-design")
def program_design():
    return render_template("Big Idea/Big Idea 1/program_design.html")


@app.route("/support")
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)

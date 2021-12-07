import requests
from flask import Flask, render_template
# create an instance of flask object
app = Flask(__name__)


# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")


@app.route("/abouttheexam")
def abouttheexam():
    return render_template("abouttheexam.html")


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
    url = "https://free-nba.p.rapidapi.com/players"

    querystring = {"page": "0", "per_page": "25", "search": "curry"}

    headers = {
        'x-rapidapi-host': "free-nba.p.rapidapi.com",
        'x-rapidapi-key': "199e385baamshc0a4c645191a179p191ebdjsn70f0155c5394"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    players = response.json()

    return render_template("rebecca.html", players=players)


@app.route("/Collaboration1")
def Collaboration1():
    return render_template("Big Idea/Big Idea 1/Collaboration1.html")

@app.route("/Collaboration2")
def Collaboration2():
    return render_template("Big Idea/Big Idea 2/Collaboration2.html")

@app.route("/Collaboration3")
def Collaboration3():
    return render_template("Big Idea/Big Idea 3/Collaboration3.html")

@app.route("/Collaboration4")
def Collaboration4():
    return render_template("Big Idea/Big Idea 4/Collaboration4.html")

@app.route("/Collaboration5")
def Collaboration5():
    return render_template("Big Idea/Big Idea 5/Collaboration5.html")

@app.route("/Creativedevelopment1")
def Creativedevelopment1():
    return render_template("Big Idea/Big Idea 1/Creativedevelopment1.html")

@app.route("/Creativedevelopment2")
def Creativedevelopment2():
    return render_template("Big Idea/Big Idea 2/Creativedevelopment2.html")

@app.route("/Creativedevelopment3")
def Creativedevelopment3():
    return render_template("Big Idea/Big Idea 3/Creativedevelopment3.html")

@app.route("/Creativedevelopment4")
def Creativedevelopment4():
    return render_template("Big Idea/Big Idea 4/Creativedevelopment4.html")

@app.route("/Creativedevelopment5")
def Creativedevelopment5():
    return render_template("Big Idea/Big Idea 5/Creativedevelopment5.html")

@app.route("/Programdesign1")
def Programdesign1():
    return render_template("Big Idea/Big Idea 1/Programdesign1.html")

@app.route("/Programdesign2")
def Programdesign2():
    return render_template("Big Idea/Big Idea 2/Programdesign2.html")

@app.route("/Programdesign3")
def Programdesign3():
    return render_template("Big Idea/Big Idea 3/Programdesign3.html")

@app.route("/Programdesign4")
def Programdesign4():
    return render_template("Big Idea/Big Idea 4/Programdesign4.html")

@app.route("/Programdesign5")
def Programdesign5():
    return render_template("Big Idea/Big Idea 5/Programdesign5.html")

@app.route("/support")
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)

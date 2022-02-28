from flask import Blueprint, render_template, request
from .trivia import Trivia

nba = Blueprint('nba', __name__,
                url_prefix='/nba',
                template_folder='templates',
                static_folder='static',
                static_url_path='assets')

# default set of players and teams
ath = ["Joel Embiid", "James Harden", "Tobias Harris", "Giannis Antetokounmpo", "Jrue Holiday"]
# answers are all supposed to be incorrect
ans = ["chargers", "76ers", "Los Angeles Lakers", "Bucks", "holidays"]


@nba.route('/', methods=['GET', 'POST'])
def trivia():
    if request.form:
        # Create empty list answers
        answers = []
        for i in range(1, 6):
            # Add all 5 of user's answers to list answers
            answers.append(request.form.get('team' + str(i)))
        athletes = ['Joel Embiid', 'LeBron James', 'Stephen Curry', 'Giannis Antetokounmpo', 'Luka Doncic']
        return render_template("nba.html", result=Trivia(answers, athletes))
    return render_template("nba.html", result=Trivia(ans, ath))



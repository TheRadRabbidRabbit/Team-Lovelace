from flask import Blueprint, render_template

nba = Blueprint('nba', __name__,
                url_prefix='/nba',
                template_folder='templates',
                static_folder='nba/static',
                static_url_path='assets')


@nba.route('/')
def trivia():
    return render_template("nba.html")

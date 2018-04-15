from flask import render_template
from . import main


@main.app_errorhandler(404)
def fourOfour(e):
    return render_template('fourOfour.html'), 404


@main.app_errorhandler(500)
def fiveOfive(e):
    return render_template('fiveOfive.html'), 500

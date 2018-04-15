from flask import render_template
from . import main
from ..requests import get_sources, get_articles


@main.route('/')
def index():
    return render_template('')

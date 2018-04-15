from flask import render_template
from . import main
from ..requests import get_sources, get_articles


@main.route('/')
def index():
    general_list = get_sources('us', 'general')
    business_list = get_sources('us', 'business')
    technology_list = get_sources('us', 'technology')
    sports_list = get_sources('us', 'sports')
    science_list = get_sources('us', 'science')
    enterntainment_list = get_sources('us', 'enterntainment')
    health_list = get_sources('us', 'health')
    return render_template('index.html', general=general_list, business=business_list, technology=technology_list, sports=sports_list, scince=science_list, entertainment=enterntainment_list, health=health_list)

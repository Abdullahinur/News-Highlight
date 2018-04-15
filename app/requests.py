import urllib.request
import json
from .models import Articles
from .models import Sources


api_key = None

source_url = None
article_url = None


def configure_requests(app):
    global api_key, source_url, article_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_SOURCES_URL']
    article_url = app.config['NEWS_ARTICLE_URL']


def get_sources(country, category):
    get_sources_url = source_url.format(country, category, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_result = None

        if get_sources_response['sources']:
            sources_result_list = get_sources_response['sources']
            sources_result = process_results(sources_result_list)

    return sources_result


def process_results(sources_list):
    sources_result = []

    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        print(id)
        title = sources_item.get('title')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        country = sources_item.get('country')

        if url:
            sources_object = Sources(id, name, title, description, url, category, country)
            sources_result.append(sources_object)

    return sources_result


def get_articles(id):
    get_articles_url = article_url.format(id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:

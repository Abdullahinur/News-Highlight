import os


class Config:
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_SOURCES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


class ProdConfig(Config):
    pass


class Devconfig(Config):
    debug = True


config_options = {
    'development': Devconfig,
    'production': ProdConfig
}

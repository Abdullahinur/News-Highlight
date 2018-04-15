import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Article(1234, 'Ajc.com', 'Tom Brueggemann',
                                   'Florida woman caught with cocaine in purse blames the wind', 'The answer for the cocaine in her purse, a Florida woman allegedly said, was blowing in the wind.', 'https://www.ajc.com/rf/image_large/Pub/p9/CmgSharedContent/2018/04/08/Images/posey.jpg"', '"https://www.ajc.com/news/florida-woman-caught-with-cocaine-purse-blames-the-wind/jop6WQ5lm6ycerbqdkNvUP/"', '2018-04-08')

    def test_instance(self):
        self.assertTrue(isinstance(self.))

from handler.base import BaseHandler
from handler.province import ProvinceHandler
from handler.city import LikedCityHandler, LikedCityInsertHandler
from handler.login import LoginHandler
from handler.signup import SignupHandler
from settings import settings

url_patterns = [
    (r"/login", LoginHandler),
    (r"/signup", SignupHandler),
    (r"/username/city/add", LikedCityInsertHandler),
    (r"/username/city", LikedCityHandler),
    (r"/province/(?P<province>.*)", ProvinceHandler),
    (r"/.*", BaseHandler)
]

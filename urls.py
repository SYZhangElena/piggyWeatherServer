from handler.base import BaseHandler
from handler.provinceHandler import ProvinceHandler
from settings import settings

url_patterns = [
    (r"/province/(?P<province>.*)", ProvinceHandler),
    (r"/.*", BaseHandler)
]

from handler.base import BaseHandler
from settings import settings

url_patterns = [
    (r"/.*", BaseHandler)
]

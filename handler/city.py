import logging
import json

import utils.db as db
from base import BaseHandler


class LikedCityHandler(BaseHandler):

    def prepare(self):
        super(LikedCityHandler, self).prepare()

    def post(self):
        res = {
            'cities': []
        }

        logging.info(self.request.body)
        try:
            params = json.loads(self.request.body)
        except:
            logging.info('Invalid post params')
            self.write(res)
            return

        if 'username' not in params:
            self.write(res)
            return

        try:
            cities = db.get_cities_by_username(params['username'])
        except Exception as why:
            logging.error(why)
        else:
            res['cities'] = cities

        self.write(res)


class LikedCityInsertHandler(BaseHandler):
    def prepare(self):
        super(LikedCityInsertHandler, self).prepare()

    def post(self):
        res = {
            'retcode': 1
        }

        logging.info(self.request.body)
        try:
            params = json.loads(self.request.body)
        except:
            logging.info('Invalid post params')
            self.write(res)
            return

        if 'username' not in params or 'city_cn' not in params:
            self.write(res)
            return

        try:
            cities = db.insert_liked_city(params['username'], params['city_cn'])
        except Exception as why:
            logging.error(why)
        else:
            res['retcode'] = 0

        self.write(res)



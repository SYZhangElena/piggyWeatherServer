import logging

import utils.db as db
from base import BaseHandler


class ProvinceHandler(BaseHandler):
    def prepare(self):
        super(ProvinceHandler, self).prepare()

    def get(self, province):
        try:
#            province = province.encode('utf-8')
            cities = db.get_cities_by_province(province)
        except Exception as why:
            logging.error(why)
            self.write({
                'cities': []
            })
            return
        else:
            logging.info(cities)
            self.write({
                'cities': cities
            })

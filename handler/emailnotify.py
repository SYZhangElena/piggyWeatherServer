import logging
import json

import utils.db as db
from base import BaseHandler


class EmailNotifyHandler(BaseHandler):

    def prepare(self):
        super(EmailNotifyHandler, self).prepare()

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

        if 'username' not in params or 'email' not in params or 'city_cn' not in params:
            self.write(res)
            return

        try:
            cities = db.insert_email_city(params['email'], params['username'], params['city_cn'])
        except Exception as why:
            logging.error(why)
        else:
            res['retcode'] = 0

        self.write(res)



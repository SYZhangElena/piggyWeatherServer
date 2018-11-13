import logging
import json
import datetime

import utils.db as db
from base import BaseHandler


class TmpMapHandler(BaseHandler):

    def prepare(self):
        super(TmpMapHandler, self).prepare()
        self.BASE_URL = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_WEAP_S99_ETO_TWC_L88_P9_'

    def get(self):
        # http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_WEAP_S99_ETO_TWC_L88_P9_20181113090000000.JPG
        now = datetime.datetime.now()
        postfix = now.strftime('%Y%m%d%H0000000')
        url = '{0}/{1}.JPG'.format(self.BASE_URL, postfix)
        self.write({
            'imgs': [url]
        })


# conding = utf-8

import sqlite3
from sqlite3 import Error
import logging
import traceback
from io import StringIO
import os

#from settings import settings

#config = settings['config']
#DATABASE = config.get('sqlite', 'MATRIX_DB_FILE').strip('""')

DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATABASE = os.path.join(DIR, 'piggyWeather.db')

def trace(f):
    def _trace(*args, **kwargs):
        try:
            res = f(*args, **kwargs)
        except:
            fp = StringIO()
            traceback.print_exc(file=fp)
            logging.exception(fp.getvalue())
            res = None
        return res
    return _trace


class ConnectionSingleton(object):
    conn = None

    def __new__(cls, **kwargs):
        print(kwargs)
        cls.database = kwargs.get('database', DATABASE)
        if cls.conn is None:
            cls.conn = sqlite3.connect(cls.database)
        return cls.conn


@trace
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = ConnectionSingleton(database=DATABASE)
        return conn
    except Error as e:
        logging.error(e)
    return None


@trace
def get_cities_by_province(province):
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT city_en FROM cities where province_cn=?", (province,))
        rows = cur.fetchall()
    logging.info(rows)
    res = []
    for row in rows:
        if row:
            res.append(row[0])
    return res


@trace
def get_cityid_by_citycn(city_cn):
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT city_id FROM cities where city_cn = ?", (city_cn,))
        row = cur.fetchone()
    logging.info(row)
    if not row:
        return None
    else:
        return row[0]


@trace
def get_cities_by_username(username):
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT distinct city_cn FROM likedcities, cities WHERE likedcities.username = ? AND likedcities.city_id = cities.city_id", (username,))
        rows = cur.fetchall()
    logging.info(rows)
    res = []
    for row in rows:
        if row:
            res.append(row[0])
    return res


@trace
def get_passwd_by_username(username):
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT passwd FROM user WHERE username=?", (username,))
        row = cur.fetchone()
    logging.info(row)
    if not row:
        return None
    else:
        return row[0]


@trace
def insert_user(username, passwd):
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE username=?", (username,))
        t = cur.fetchone()
        if t:
            return None
        cur.execute("INSERT INTO user (username, passwd) VALUES (?, ?)", (username, passwd,))
    return cur.lastrowid


@trace
def insert_liked_city(username, city_cn):
    city_id = get_cityid_by_citycn(city_cn)
    if not city_id:
        logging.info('No such city found: {0}'.format(city_cn))
        return None
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO likedcities (username, city_id) VALUES (?, ?)", (username, city_id))
    return cur.lastrowid


@trace
def insert_email_city(email, username, city_cn):
    city_id = get_cityid_by_citycn(city_cn)
    if not city_id:
        logging.info('No such city found: {0}'.format(city_cn))
        return None
    logging.info('get city_id: {0}'.format(city_id))
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO cityemail (email, username, city_id) VALUES (?, ?, ?)", (email, username, city_id,))
    return cur.lastrowid


@trace
def get_all_email_city_list():
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT * FROM cityemail")
        rows = cur.fetchall()
    return rows


@trace
def get_user_list():
    conn = create_connection(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")
        rows = cur.fetchall()
    res = []
    for row in rows:
        if row:
            print(row)
            res.append((row[0], row[1]))
    return res


if __name__ == '__main__':
#    res = insert_user('heihei', 'heiheiheihei')
#    print(res)
#    print(get_user_list())
#    print(get_cities_by_username('zhangshuyu'))
#    print(get_passwd_by_username('zhangshuyu'))
    print(DATABASE)
    print(get_all_email_city_list())

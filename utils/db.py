# conding = utf-8

import sqlite3
from sqlite3 import Error
import logging

#from settings import settings

#DATABASE = settings['config']['sqlite']['MATRIX_DB_FILE']
DATABASE = '/home/eric/SarKerson/pythonthon/piggyServer/piggyWeather.db'

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        logging.error(e)
    return None


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



def main():
    conn = create_connection(DATABASE)
    r = get_cities_by_province('北京')
    print(r)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM cities limit 20")
        rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()

import pymysql


def db_connect():
    db = pymysql.connect(host="localhost", user="root", password="jinhong", db="korail_talk", charset="utf8")
    cursor = db.cursor()

    return db, cursor
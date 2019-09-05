import pymysql
from DB.connect import db, cursor
from flask_restful import reqparse


def get():
    return_dict = {}
    count = 1

    reqp = reqparse.RequestParser()
    reqp.add_argument('start', type=str)
    reqp.add_argument('end', type=str)
    reqp.add_argument('time', type=str)
    reqp.add_argument('date', type=str)

    args = reqp.parse_args()

    start = args['start']
    end = args['end']
    time = args['time']
    date = args['date']

    sql = f'SELECT Train_Num, Train_Name, {start}, {end} FROM FromSeoulToBusan WHERE {start} != "NULL" AND {end} != "NULL"'
    cursor.execute(sql)
    train_inform = list(cursor.fetchall())

    for specific in train_inform:
        specific_dict = {}
        specific_dict['train_num'] = specific[0]
        specific_dict['train_name'] = specific[1]
        specific_dict['start_time'] = specific[2]
        specific_dict['end_time'] = specific[3]

        return_dict[count] = specific_dict
        count += 1

    return return_dict
import pymysql
import datetime
from DB.connect import db, cursor
from flask_restful import reqparse

date_dict = {
    "Monday": '1',
    "Tuesday": '2',
    "Wednesday": '3',
    "Thursday": '4',
    "Friday": '5',
    "Saturday": '6',
    "Sunday": '7'
}


def get():
    return_dict = {}
    count = 1

    reqp = reqparse.RequestParser()
    reqp.add_argument('start', type=str)
    reqp.add_argument('end', type=str)
    reqp.add_argument('date', type=str)

    args = reqp.parse_args()

    now = datetime.datetime.now()
    start = args['start']
    end = args['end']
    time = now.strftime("%H%M")
    date = args['date']

    dt = datetime.date(int(date[0:4]), int(date[4:6]), int(date[6:8]))

    sql = f'SELECT Train_Num, Train_Name, {start}, {end}, Remark FROM FromSeoulToBusan WHERE {start} != "NULL" AND {end} != "NULL"'
    cursor.execute(sql)
    train_inform = list(cursor.fetchall())

    for specific in train_inform:
        if specific[4] != None and date_dict[dt.strftime("%A")] not in str(specific[4]):
            continue

        if date == now.strftime("%Y%m%d"):
            if (specific[2] // 100) * 60 + (specific[2] % 100) < (int(time)//100 * 60 + int(time) % 100):
                continue

        specific_dict = {}
        specific_dict['train_num'] = specific[0]
        specific_dict['train_name'] = specific[1]

        time_list = [str(specific[2]), str(specific[3])]
        time_real_list = []

        for i in time_list:
            if len(i) != 4:
                for _ in range(4 - len(i)):
                    i = '0' + i
                i = i[:2] + ":" + i[2:]
                if i[:1] == '0':
                    i = i[1:]
            else:
                i = i[:2] + ":" + i[2:]

            time_real_list.append(i)

        specific_dict['start_time'] = time_real_list[0]
        specific_dict['end_time'] = time_real_list[1]

        return_dict[count] = specific_dict
        count += 1


    sql = "SELECT * FROM TrainFare"
    cursor.execute(sql)
    print(cursor.fetchall())

    return return_dict
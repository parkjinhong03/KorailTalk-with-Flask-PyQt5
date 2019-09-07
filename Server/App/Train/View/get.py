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

train_korean_name = {
        'Seoul': '서울',
        'Gwangmyeong': '광명',
        'Cheonan_Asan': '천안아산',
        'Osong': '오송',
        'Daejeon': '대전',
        'Gimcheon_Gumi': '김천구미',
        'Dongdaegu': '동대구',
        'Singyeongju': '신경주',
        'Ulsan': '울산',
        'Busan': '부산'
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
        date1 = datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]), specific[2]//100, specific[2]%100, 0)
        date2 = datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]), specific[3]//100, specific[3]%100, 0)
        train_take_time = str(date2-date1)

        if len(train_take_time) < 8:
            specific_dict['operating_time'] = train_take_time[:4]

        elif len(train_take_time) > 9:
            specific_dict['operating_time'] = train_take_time[8:12]
            print(train_take_time)

        return_dict[count] = specific_dict
        count += 1


    sql = f'SELECT * FROM TrainFare WHERE Intersection = "{train_korean_name[start]}_{train_korean_name[end]}"'
    cursor.execute(sql)

    fare_dict = {}
    fare_data = cursor.fetchone()

    fare_dict['general'] = fare_data[1]
    fare_dict['special'] = fare_data[2]

    return_dict['fare'] = fare_dict

    return return_dict
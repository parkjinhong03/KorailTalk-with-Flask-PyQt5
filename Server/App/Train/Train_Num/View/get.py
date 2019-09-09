from flask_restful import reqparse
from DB.connect import db, cursor

train_to_num = {
        'Seoul': 1,
        'Gwangmyeong': 2,
        'Cheonan_Asan': 3,
        'Osong': 4,
        'Daejeon': 5,
        'Gimcheon_Gumi': 6,
        'Dongdaegu': 7,
        'Singyeongju': 8,
        'Ulsan': 9,
        'Busan': 10
    }


def get(date):
    return_dict = {}

    req = reqparse.RequestParser()
    req.add_argument('train_num', type=str)
    req.add_argument('start', type=str)
    req.add_argument('end', type=str)

    args = req.parse_args()

    train_num = args['train_num']
    start = args['start']
    end = args['end']

    sql = f'SELECT * FROM K{date} WHERE train_num = {train_num}'

    try:
        cursor.execute(sql)

    except:
        for i in range(40):
            return_dict[str(i + 1)] = '0'
        return return_dict

    seat_data = list(cursor.fetchall())

    for i in range(40):
        count = 0
        specific_data = list(seat_data[i])
        for j in range(train_to_num[start], train_to_num[end]):
            if specific_data[j+1] == 1:
                return_dict[str(i+1)] = '1'
                count += 1
                break
        if count == 0:
            return_dict[str(i+1)] = '0'

    return return_dict
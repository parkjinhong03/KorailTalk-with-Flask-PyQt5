from flask_restful import reqparse
from DB.connect import db, cursor


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

    print(date, train_num, start, end)

    sql = f'SELECT * FROM K{date} WHERE train_num = "{train_num}"'

    try:
        cursor.execute(sql)

    except:
        for i in range(40):
            return_dict[str(i + 1)] = '0'
        return return_dict

    return '이제 시작이다.'
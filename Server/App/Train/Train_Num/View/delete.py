from flask_restful import reqparse
from flask_jwt_extended import get_jwt_identity
from DB.connect import db, cursor


def delete(date):
    reqp = reqparse.RequestParser()

    reqp.add_argument('train_num', type=str)
    reqp.add_argument('seat', type=str)
    reqp.add_argument('start', type=str)
    reqp.add_argument('end', type=str)

    args = reqp.parse_args()

    _id = get_jwt_identity()
    train_num = args['train_num']
    seat = args['seat']
    start = args['start']
    end = args['end']

    print(_id, date, train_num, seat, start, end)

    sql = f'SELECT * FROM reservation WHERE id = "{_id}" AND date = "{date}" AND train_num = "{train_num}" AND start = "{start}" AND end = "{end}"'

    cursor.execute(sql)
    search_data = cursor.fetchone()

    if search_data == None:
        return {"Message": "예매 X"}, 422

    sql = f'DELETE FROM reservation WHERE id = "{_id}" AND date = "{date}" AND train_num = "{train_num}" AND start = "{start}" AND end = "{end}"'

    cursor.execute(sql)

    return 'ok!', 200
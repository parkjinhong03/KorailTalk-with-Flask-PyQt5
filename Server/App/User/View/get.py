from flask_jwt_extended import get_jwt_identity
from DB.connect import db, cursor
import json


def get():
    _userID = get_jwt_identity()
    return_dict = {}
    count = 0

    sql = f'SELECT * FROM reservation WHERE id = "{_userID}"'
    cursor.execute(sql)

    reservation_data = list(cursor.fetchall())

    for i in reservation_data:
        specific_dict = {}

        count += 1

        specific_dict['date'] = i[1]
        specific_dict['train_num'] = i[2]
        specific_dict['seat'] = i[3]
        specific_dict['start'] = i[4]
        specific_dict['end'] = i[5]

        return_dict[count] = specific_dict

    return return_dict
from flask_restful import reqparse
from DB.connect import db, cursor


def post(date):
    return_dict = {}

    req = reqparse.RequestParser()
    req.add_argument('train_num', type=str)
    req.add_argument('start', type=str)
    req.add_argument('end', type=str)
    req.add_argument('seat', type=int)

    args = req.parse_args()

    train_num = args['train_num']
    start = args['start']
    end = args['end']
    seat = args['seat']

    create_table(date)

    print(date, train_num, start, end, seat)

    return return_dict


def create_table(date):
    sql = f"CREATE TABLE K{str(date)} (" \
        f"Train_Num TEXT NOT NULL," \
        f"Seat TEXT NOT NULL," \
        f"Seoul INT NOT NULL DEFAULT 0," \
        f"Gwangmyeong INT NOT NULL DEFAULT 0," \
        f"Cheonan_Asan INT NOT NULL DEFAULT 0," \
        f"Osong INT NOT NULL DEFAULT 0," \
        f"Daejeon INT NOT NULL DEFAULT 0," \
        f"Gimcheon_Gumi INT NOT NULL DEFAULT 0," \
        f"Dongdaegu INT NOT NULL DEFAULT 0," \
        f"Singyeongju INT NOT NULL DEFAULT 0," \
        f"Ulsan INT NOT NULL DEFAULT 0," \
        f"Busan INT NOT NULL DEFAULT 0" \
        f")"

    try:
        cursor.execute(sql)
    except:
        return

    count = 0

    train_num_list = [101, 271, 103, 105, 201, 291, 107, 109, 111, 113, 115, 231, 117, 119, 251, 121, 273, 123,
                      233, 125, 127, 129, 131, 253, 133, 135, 203, 293, 137, 205, 295, 139, 207, 141, 209, 143,
                      145, 147, 235, 149, 255, 151, 153, 155, 157, 257, 159, 211, 161, 237, 275, 213, 163, 215,
                      165, 167, 259, 169, 261, 171, 173, 217, 281, 283]

    for i in train_num_list:
        for j in range(40):
            sql = f'INSERT INTO k{date} (Train_Num, Seat) VALUES({i}, {j+1})'
            cursor.execute(sql)

    print(count)
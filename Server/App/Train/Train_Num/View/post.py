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
    train_status_list = train_list(start, end)

    sql = f'SELECT * FROM k{date} WHERE Train_Num = "{train_num}" AND Seat = "{seat}"'
    cursor.execute(sql)
    seat_data = list(cursor.fetchone())

    for i in range(train_to_num[start], train_to_num[end]):
        if seat_data[i+1] == 1:
            return '여기는 예약이 불가능함용'

    print(seat_data)

    sql = f'UPDATE k{date} SET  SeoulToGwangmyeong = {train_status_list[0]}, GwangmyeongToCheonan_Asan  = {train_status_list[1]}, Cheonan_AsanToOsong  = {train_status_list[2]}, ' \
        f'OsongToDaejeon = {train_status_list[3]}, DaejeonToGimcheon_Gumi = {train_status_list[4]}, Gimcheon_GumiToDongdaegu  = {train_status_list[5]}, DongdaeguToSingyeongju  = {train_status_list[6]},' \
        f'SingyeongjuToUlsan = {train_status_list[7]}, UlsanToBusan = {train_status_list[8]} WHERE Train_Num = "{train_num}" AND Seat = "{seat}"'
    cursor.execute(sql)

    print(train_status_list)
    print(date, train_num, start, end, seat)

    return f'{str(date)[:4]}년 {str(date)[4:6]}월 {str(date)[6:8]}일 {train_num}번 기차 {seat}좌석 예매를 성공했습니다.', 200


def train_list(start, end):

    return_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(train_to_num[start], train_to_num[end]):
        return_list[i-1] = 1

    return return_list


def create_table(date):
    sql = f"CREATE TABLE K{str(date)} (" \
        f"Train_Num TEXT NOT NULL," \
        f"Seat TEXT NOT NULL," \
        f"SeoulToGwangmyeong INT NOT NULL DEFAULT 0," \
        f"GwangmyeongToCheonan_Asan INT NOT NULL DEFAULT 0," \
        f"Cheonan_AsanToOsong INT NOT NULL DEFAULT 0," \
        f"OsongToDaejeon INT NOT NULL DEFAULT 0," \
        f"DaejeonToGimcheon_Gumi INT NOT NULL DEFAULT 0," \
        f"Gimcheon_GumiToDongdaegu INT NOT NULL DEFAULT 0," \
        f"DongdaeguToSingyeongju INT NOT NULL DEFAULT 0," \
        f"SingyeongjuToUlsan INT NOT NULL DEFAULT 0," \
        f"UlsanToBusan INT NOT NULL DEFAULT 0" \
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
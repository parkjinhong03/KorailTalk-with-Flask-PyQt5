Seoul = {
    "광명": {
        "price": {
            "general": 8400,
            "special": 13200
        },
        "train": {
            1: {
                "TrainNum": 101,
                "TrainName": 'KTX',
                "StartTime": "5:15",
                "EndTime": "5:31",
            }
        }
    }
}

import pymysql

db = pymysql.connect(host="localhost", user='root', password="jinhong", db="korail_talk")

cur = db.cursor()

sql =  'SELECT Train_Num FROM FromSeoulToBusan WHERE Train_Name = "KTX-산천"'
cur.execute(sql)

print(cur.fetchone())
cur.close()
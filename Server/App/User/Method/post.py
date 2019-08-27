from flask_restful import reqparse
from flask_jwt_extended import create_access_token
import pymysql
from DB.connect import db_connect
from DB.User.id_exist import id_exist


def signup():
    '''
    id와 pw, pw_check을 받아서 회원을 등록시켜주는 POST Method
    :parameter: id, pw, pw_check
    :return: status code
    200 - 성공
    410 - 이미 사용중인 ID
    411 - 비밀번호 입력 오류
    '''

    try:
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('pw', type=str)
        parser.add_argument('pw_check', type=str)
        args = parser.parse_args()

        _userId = args['id']
        _userPw = args['pw']
        _userPw_check = args['pw_check']

        db, cursor = db_connect()


        sql = '''
            CREATE TABLE userlog (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id  TEXT NOT NULL,
                user_pw TEXT NOT NULL
            )'''

        try:
            cursor.execute(sql)
        except:
            pass

        if _userPw != _userPw_check:
            return {"message": "pw and pw_check do not match.", "code": 411}, 411

        if id_exist(db, cursor, _userId) == True:
            return {"message": "This ID is already in use.", "code": 410}, 410

        sql = f'INSERT INTO userlog (user_id, user_pw) VALUES("{_userId}", "{_userPw}")'
        cursor.execute(sql)

        db.commit()
        db.close()

        return {"message": "Your ID has been successfully registered!", "code": 200}, 200

    except SyntaxError as e:
        return {'error':str(e)}


def login():
    '''
    id와 pw를 받아서 로그인을 헤주는 POST Method
    :parameter: id, pw
    :return: status code
    200 - 로그인 성공
    410 - ID 입력 오류
    411 - PW 입력 오류
    '''
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('pw', type=str)
        args = parser.parse_args()
        _userID = args['id']
        _userPW = args['pw']

        db, cursor = db_connect()

        if id_exist(db, cursor, _userID) == False:
            return {"message": "Invalid ID entered.", "code": 410}, 410

        sql = f'SELECT user_pw FROM UserLog WHERE user_id = "{_userID}"'
        cursor.execute(sql)

        if _userPW != cursor.fetchone()[0]:
            return {"message": 'Wrong PW entered.', "code": 411}, 411
        else:
            access_token = create_access_token(identity=_userID)
            return {"access_token": access_token, "code": 200}, 200

    except Exception as e:
        return {"error": str(e)}, 400
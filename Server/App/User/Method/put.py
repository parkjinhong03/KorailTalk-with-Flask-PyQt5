from flask_restful import reqparse
from flask_jwt_extended import get_jwt_identity
import pymysql
from DB.connect import db_connect


def put():
    '''
    회원의 password를 바꿔주는 PUT Method
    :parameter: pw, pw_check
    :return: status code
    200 - 성공
    401 - JWT 존재 X or 만료됨
    422 - JWT Decoding 오류
    411 - 비밀번호 확인 불일치
    '''

    parser = reqparse.RequestParser()
    parser.add_argument('pw', type=str)
    parser.add_argument('pw_check', type=str)
    args = parser.parse_args()

    _userPw = args['pw']
    _userPwC = args['pw_check']

    if _userPw != _userPwC:
        return {"message": "pw and pw_check do not match", "code": 411}, 411

    current_user = get_jwt_identity()

    db, cursor = db_connect()

    sql = f'UPDATE userlog SET user_pw = "{_userPw}"  WHERE user_id = "{current_user}"'
    cursor.execute(sql)

    db.commit()
    db.close()

    return {"message": "Your password has changed normally.", "code": 200}, 200
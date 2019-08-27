from flask_jwt_extended import get_jwt_identity
from DB.connect import db_connect
from DB.User.id_exist import id_exist


def delete():
    '''
    회원 탈퇴를 위한 DELETE Method
    :parameter: X
    :return: status code
    200 - 성공
    401 - JWT 토큰 X or 만료
    422 - JWT 디코딩 오류
    410 - 해당 계정이 존재하지 않음.
    '''

    current_user = get_jwt_identity()

    db, cursor = db_connect()

    if id_exist(db, cursor, current_user) == False:
        return {"message": "The account does not exist.", "code": 410}, 410

    sql = f'DELETE FROM userlog WHERE user_id="{current_user}"'

    cursor.execute(sql)
    db.commit()
    db.close()

    return {"message": "Deleting account completed successfully.", "code": 200}, 200
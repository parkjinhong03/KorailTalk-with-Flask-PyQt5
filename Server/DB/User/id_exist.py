import pymysql


def id_exist(db, cursor, user_id):
    sql = f'SELECT EXISTS (SELECT * FROM userlog where user_id="{user_id}") as success;'
    cursor.execute(sql)

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False
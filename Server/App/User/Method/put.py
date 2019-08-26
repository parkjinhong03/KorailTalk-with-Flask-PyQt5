from flask_restful import reqparse


def put():
    '''
    회원의 password를 바꿔주는 PUT Method
    :parameter: pw, pw_check
    :return: status code
    200 - 성공
    '''

    parser = reqparse.RequestParser()
    parser.add_argument('pw', type=str)
    parser.add_argument('pw_check', type=str)
    args = parser.parse_args()

    print(args['pw'], args['pw_check'])

    return 'ok'
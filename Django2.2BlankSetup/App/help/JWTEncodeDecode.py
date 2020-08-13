'''
    Help Package
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''

# pip install PyJWT
import jwt


def Encode_HS256(payload):
    jwt_token = {'token': jwt.encode(payload, 'secret', algorithm='HS256')}
    return jwt_token['token'].decode("utf-8")


def Decode_HS256(token):
    jwt_token = jwt.decode(token, 'secret', algorithms=['HS256'])
    return jwt_token


def Encode_HS512(payload):
    jwt_token = {'token': jwt.encode(payload, 'secret', algorithm='HS512')}
    return jwt_token['token'].decode("utf-8")


def Decode_HS512(token):
    jwt_token = jwt.decode(token, 'secret', algorithms=['HS512'])
    return jwt_token
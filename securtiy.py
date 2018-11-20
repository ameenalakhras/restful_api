from user import User
from werkzeug.security import safe_str_cmp # compares two strings if they're equal


users= [User(1,'bob','pass123')]

username_mapping = {usr.username : usr for usr in users}

userid_mapping = {usr.id : usr for usr in users}

def authenticate(username,password):
    """search users by username and make sure of the password"""
    user = username_mapping.get(username,None)

    if user and (user.password,password) :
        return user


def identity(payload):
    """search users by id"""
    user_id = payload['identity']
    return userid_mapping.get(user_id,None)

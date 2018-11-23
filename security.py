from models.user import UserModel
from werkzeug.security import safe_str_cmp # compares two strings if they're equal

### find by username
def authenticate(name, password):
    user = UserModel.find_by_name(name)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

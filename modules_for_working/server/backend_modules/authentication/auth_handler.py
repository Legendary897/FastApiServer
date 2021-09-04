import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
# from modules_for_working.db_modules.pymongo_chouse.work_with_db import DataFlowWithDB as db
from modules_for_working.db_modules.mongoegine_chouse.work_with_db import DataFlowWithDB as db
from modules_for_working.models.model_for_mongo import UserForMongo as model_db
from modules_for_working.models.user_model import User


class AuthHand(object):

    def __init__(self):
        self.security = HTTPBearer()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.secret = "SECRET"

    def login(self, user_details):
        user = None
        exist_user = db().get_username(user_details.username)
        if exist_user is not None:
            if self._verify_password(user_details.password, exist_user["password"]):
                return {'token': self._encode_token(exist_user['username'], exist_user['role'])}
        raise HTTPException(status_code=401, detail='Invalid username or password')

    def registration(self, user_details):
        db_con = db()
        if db_con.get_username(user_details.username) is None:
            user_details.password = self._get_password_hash(user_details.password)
            if type(user_details) == type(User):
                db_con.add_new_user(model_db.create_spec_data_format_registration(user_details))
            else:
                db_con.add_new_user(model_db.create_spec_data_format_add_admin(user_details))
            return {"message": "Ok"}
        else:
            raise HTTPException(status_code=400, detail='username is taken!')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(HTTPBearer())):
        return self._decode_token(auth.credentials)

    def auth_shared_access(self, auth: HTTPAuthorizationCredentials = Security(HTTPBearer())):
        role = self._decode_token(auth.credentials)
        if role == 1:
            return True
        else:
            return False

    def _encode_token(self, username, role):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub1': username,
            'sub2': role
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def _decode_token(self, token):
        try:
            return jwt.decode(token, self.secret, algorithms=['HS256'])["sub2"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

    def _verify_password(self, raw_password, hash_password):
        return self.pwd_context.verify(raw_password, hash_password)

    def _get_password_hash(self, password):
        return self.pwd_context.hash(password)

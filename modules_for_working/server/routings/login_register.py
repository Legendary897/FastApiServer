from fastapi import APIRouter
from modules_for_working.models.user_model import User, UserForAuth
from modules_for_working.server.backend_modules.authentication.auth_handler import AuthHand

route_login = APIRouter()


@route_login.post('/register', status_code=201)
def register(auth_details: User):
    return AuthHand().registration(auth_details)


@route_login.post('/login')
def login(auth_details: UserForAuth):
    return AuthHand().login(auth_details)

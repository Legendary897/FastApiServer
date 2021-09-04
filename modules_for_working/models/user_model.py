from pydantic import BaseModel


class UserData(BaseModel):
    name: str
    surname: str
    old: int


class User(BaseModel):
    username: str
    password: str
    user_data: UserData


class UserForAuth(BaseModel):
    username: str
    password: str


class UserAddForAdmin(BaseModel):
    username: str
    password: str
    role: int
    user_data: UserData
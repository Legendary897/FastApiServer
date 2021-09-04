from fastapi import APIRouter, Depends, HTTPException
from modules_for_working.server.backend_modules.authentication.auth_handler import AuthHand
from modules_for_working.models.user_model import UserAddForAdmin, UserData
from modules_for_working.db_modules.pymongo_chouse.work_with_db import DataFlowWithDB as db
# from modules_for_working.db_modules.mongoegine_chouse.work_with_db import DataFlowWithDB as db
from modules_for_working.models.model_for_mongo import UserForMongo
from modules_for_working.server.backend_modules.check_id import TryReformatId

route_for_data_users = APIRouter()
auth_handler = AuthHand()


@route_for_data_users.post('/add_user')
def add_user(auth_details: UserAddForAdmin, flag_access=Depends(auth_handler.auth_shared_access)):
    if flag_access:
        auth_handler.registration(auth_details)
        return {"ans": "Ok!"}
    raise HTTPException(status_code=400, detail='Not enough access rights')


@route_for_data_users.get("/all_users")
def get_all_users(_=Depends(auth_handler.auth_wrapper)):
    return db().get_user_data()


@route_for_data_users.post("/delete_user")
def delete_user(_id: str, flag_access=Depends(auth_handler.auth_shared_access)):
    if flag_access:
        db().delete_cur_user(TryReformatId.reformat_id(_id))
        return {"ans": "Ok!"}
    raise HTTPException(status_code=400, detail='Not enough access rights')


@route_for_data_users.post("/update_user_info")
def update_user_info(_id: str, user_data: UserData, flag_access=Depends(auth_handler.auth_shared_access)):
    if flag_access:
        db().update_user_data(TryReformatId.reformat_id(_id), UserForMongo.create_spec_user_data(user_data))
        return {"ans": "Ok!"}
    raise HTTPException(status_code=400, detail='Not enough access rights')

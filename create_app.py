from fastapi import FastAPI
from modules_for_working.server.routings.login_register import route_login
from modules_for_working.server.routings.working_with_users import route_for_data_users
from modules_for_working.server.routings.get_json_data_from_far_servers import route_for_json_data


def init_app():
    app = FastAPI()
    app.include_router(route_login)
    app.include_router(route_for_data_users)
    app.include_router(route_for_json_data)
    return app

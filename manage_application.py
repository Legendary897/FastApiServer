from uvicorn import run
from create_app import init_app
from modules_for_working.server.settings_server import settings

if __name__ == "__main__":
    run(init_app(), port=settings["port"], host=settings["host"])
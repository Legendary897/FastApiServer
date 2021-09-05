from fastapi import FastAPI
from uvicorn import run
import json


def init_app():
    app = FastAPI()

    @app.get("/get_info")
    def get_info():
        with open("data1.json", "r") as file:
            json_data = json.load(file)
        return json_data
    return app


if __name__ == "__main__":
    run(init_app(), port=3001, host="0.0.0.0")

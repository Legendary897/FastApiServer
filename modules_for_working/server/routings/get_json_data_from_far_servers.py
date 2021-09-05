from fastapi import APIRouter
from threading import Thread
import http.client
import json

route_for_json_data = APIRouter()
list_data = []


def get_json(port):
    try:
        connection = http.client.HTTPConnection('localhost', port, timeout=2)
        connection.request("GET", "/get_info")
        response = connection.getresponse()
        answer = json.loads(response.read())
        connection.close()
        list_data.append(answer)
    except BlockingIOError:
        print("Empty_data")
    except Exception:
        print("Empty_data")


@route_for_json_data.get("/get_info")
def get_info_from_json():
    t1 = Thread(target=get_json, args={3001})
    t2 = Thread(target=get_json, args={3002})
    t3 = Thread(target=get_json, args={3003})
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    ans = {**list_data[0], **list_data[1], **list_data[2]}
    sorted_tuples = sorted(ans.items(), key=lambda x: x[0])
    ans = dict(sorted_tuples)
    return ans

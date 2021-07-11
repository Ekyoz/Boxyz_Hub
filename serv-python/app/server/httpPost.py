import requests

url="http://localhost:3000/assistant"


def httpPost(command):
    try:
        return requests.post(url=url, data={
            "user" : "alexandre",
            "command" : command
        })
    except:
        return "Server is down or there is a connection error"


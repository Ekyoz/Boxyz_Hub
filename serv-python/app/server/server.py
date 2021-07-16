from flask import Blueprint, request
import requests

server = Blueprint('server', __name__)

url="http://localhost:3000/assistant"

#------Function------#

def Post(command):
    try:
        return requests.post(url=url, data={
            "user" : "alexandre",
            "command" : command
        })
    except:
        return "Server is down or there is a connection error"

#------Route------#

@server.route("/", methods=["GET"])
def home():
    return "home serv"


@server.route("/post", methods=["GET"])
def post():
    command = request.args.get("command")
    response = Post(command)
    return response

from flask import Blueprint
from flask.globals import request
from httpPost import *

serv = Blueprint('serv', __name__)

@serv.route("/", methods=["GET"])
def home():
    return "home serv"


@serv.route("/httpPost", methods=['GET'])
def test():
    command = request.args.get("command")
    httpPost(command)

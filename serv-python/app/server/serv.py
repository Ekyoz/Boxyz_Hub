from flask import Blueprint, request

serv = Blueprint('serv', __name__)

@serv.route("/", methods=["GET"])
def home():
    return "home serv"


@serv.route("/test", methods=['GET'])
def test():
    return 'test'

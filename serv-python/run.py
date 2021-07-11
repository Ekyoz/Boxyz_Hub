from flask import Flask, request
from app.android.room import *
from app.server.serv import *
import requests
import json

main = Flask(__name__)
main.register_blueprint(AppRoom, url_prefix="/room")
main.register_blueprint(serv, url_prefix="/serv")
url="http://localhost:3000/assistant"



#----------------Remote Func----------------#
@main.route("/", methods=["GET"])
def home():
    return "home main"


@main.route('/remote/func', methods = ['GET'])
def button():
    status = request.args.get('stat')
    mac = request.args.get('mac')
    with open(access_rooms, "r") as f:
        remote = json.load(f)
    if mac in num:
        if status == "1":
            try:
                requests.post(url=url, data={
                    "user" : "alexandre",
                    "command" : {str(remote[mac]["func_1"])}
                })
                return 'Ok, turn on!'
            except:
                return 'The server is down or cannot connect!'
        if status == "2":
            try:
                requests.post(url=url, data={
                    "user" : "alexandre",
                    "command" : {str(remote[mac]["func_2"])}
                })
                return 'Ok, turn on!'
            except:
                return 'The server is down or cannot connect!'
        if status == "3":
            try:
                requests.post(url=url, data={
                    "user" : "alexandre",
                    "command" : {remote[mac]["func_3"]}
                })
                return 'Ok, turn on!'
            except:
                return 'The server is down or cannot connect!'
        if status == "off":
            func_off_PR = remote[mac]["func_off"].keys()
            func_off = str(func_off_PR).strip('[]').strip('u').strip("'")
            print(func_off)
            if 1 in remote[mac]["func_off"].keys():
                try:
                    requests.post(url=url, data={
                        "user" : "alexandre",
                        "command" : {remote[mac]["func_off"]}
                    })
                    return 'Ok, turn off!'
                except:
                    return 'The server is down or cannot connect!'
            if 2 in remote[mac]["func_off"].keys():
                compt = 0
                while compt != 2:
                    compt += 1
                    try:
                        requests.post(url=url, data={
                            "user" : "alexandre",
                            "command" : {remote[mac]["func_off"][compt]}
                        })
                        return 'Ok, turn off!'
                    except:
                        return 'The server is down or cannot connect!'
        if status > 4:
            return 'You click too much time!'


    else:
        return 'Remote not exist!'

if __name__ == "__main__":
    main.run(port=3030, host='0.0.0.0', debug=True)
from os import removedirs
from flask import Flask, request, render_template, session, redirect
import requests
import json

app = Flask(__name__)

remote = json.load(open("/home/pi/Boxyz/serv-python/remote.json", "r"))
print(remote["bc:dd:c2:55:63:67"])

url="http://192.168.1.29:3000/assistant"


#--------------------------------------------Home----------------------------------------#
@app.route('/button', methods = ['GET','POST'])
def button():
    status = request.args.get('stat')
    mac = request.args.get('mac')
    if status == "on":
        requests.post(url=url, data={
            "user": "Alexandre",
            "command": "allume lampadaire alex"
        })
        print("work")
        print(mac)
        return "ok"
    elif status == "off":
        requests.post(url=url, data={
            "user": "Alexandre",
            "command": "eteint lampadaire alex"
        })
        print("work")
        return "ok"
    else:
        return "Argument missing"

if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)


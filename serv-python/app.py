from flask import Flask, request, render_template, session, redirect
import requests
import json

app = Flask(__name__)

remotejson = open("/home/alexandre/Bureau/Projet/Domotic/serv-python/remote.json", "r")
remote=json.load(remotejson)
url="http://192.168.1.29:3000/assistant"


#--------------------------------------------Home----------------------------------------#
@app.route('/remote', methods = ['GET'])
def home():
    remoteid = request.args.get('id')
    if remoteid is None:
        return remote["remote"]
    if remoteid is not None:
        return remote["remote"][remoteid]

@app.route('/status', methods = ['GET','POST'])
def status():
    status = request.args.get('stat')
    if status == "on":
        requests.post(url=url, data={
            "user": "Alexandre",
            "command": "allume lampadaire alex"
        })
        print("work")
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


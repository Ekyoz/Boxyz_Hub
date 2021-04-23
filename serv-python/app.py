from flask import Flask, request, render_template, session, redirect
import requests
import json
from remote import addremote, delremote, remotenum, access

app = Flask(__name__)
url="http://192.168.1.29:3000/assistant"


#--------------------------------------------Home----------------------------------------#
@app.route('/add_remote', methods = ['GET'])
def add_remote():
    mac = request.args.get('mac')
    name = request.args.get('name')
    func = request.args.get('func')
    ip = request.args.get('ip')
    addremote(mac, name, func, ip)
    return 'ok'


@app.route('/del_remote', methods=['GET'])
def del_remote():
    key = request.args.get('keys')
    delremote(key)
    return 'ok'

@app.route('/remote', methods=['GET'])
def remote():
    info = request.args.get('info')

    num = remotenum()
    if info == "num":
        return str(num)
    if info == "json":
        return str(open(access, "r"))
    elif info == None:
        return str(open(access, "r")), str(num)


@app.route('/button', methods = ['GET','POST'])
def button():
    status = request.args.get('stat')
    ip = request.args.get('mac')
    requests.post(url=url, data=remote)



if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)


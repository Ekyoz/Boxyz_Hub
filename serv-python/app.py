from flask import Flask, request, render_template, session, redirect
import requests
import json
from remote import addremote, delremote, access, remote_num

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
    with open(access, "r") as f:
        remote = json.load(f)
            
    for num in remote.keys():
        remote_num.append(num)

    if info == "num":
        return remote_num
    if info == "json":
        return str(remote)
    elif info == None:
        return str(remote), remote_num


@app.route('/button', methods = ['GET','POST'])
def button():
    status = request.args.get('stat')
    ip = request.args.get('mac')
    requests.post(url=url, data=remote)



if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)


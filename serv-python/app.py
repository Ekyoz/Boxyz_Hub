from flask import Flask, request, render_template, session, redirect
import requests
import json
from remote import addremote, delremote, remote_info

app = Flask(__name__)
url="http://192.168.1.29:3000/assistant"
info_stat = remote_info()
print(info_stat)



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
    if info is None:
        return remote_info()
    if info == "json":
        return remote_info(json)
    elif info == "num":
        return remote_info(num)
    else:
        return 'Argument invalid'


@app.route('/button', methods = ['GET','POST'])
def button():
    status = request.args.get('stat')
    ip = request.args.get('mac')
    requests.post(url=url, data=remote)



if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)


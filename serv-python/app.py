from flask import Flask, request, render_template, session, redirect, jsonify
from remote import addremote, delremote, remotenum, access_remote, url, access_user
import requests
import json
import unicodedata

app = Flask(__name__)


#--------------------------------------------Remote----------------------------------------#
@app.route('/remote', methods=['GET'])
def remote():
    info = request.args.get('info')
    num = remotenum()
    with open(access_remote, "r") as f:
        remote = json.load(f)
    if info == "num":
        return str(num)
    if info == "json":
        return jsonify(str(remote))
    if info is None or info == "":
        return 'Argument missing!'


#--------------------------------------------Add remote----------------------------------------#
@app.route('/add_remote', methods = ['GET'])
def add_remote():
    mac = request.args.get('mac')
    name = request.args.get('name')
    func_1 = request.args.get('func_1')
    func_2 = request.args.get('func_2')
    func_3 = request.args.get('func_3')
    func_off = request.args.get('func_off')
    ip = request.args.get('ip')
    with open(access_remote, "r") as f:
        remote = json.load(f)
    if mac in remote:
        return 'Already exist'
    if mac and name and func_1 and func_2 and func_3 and func_off and ip is not None:
        addremote(mac, name, func_1, func_2, func_3, func_off, ip)
        return 'Ok, remote was added with mac: ' + mac +'.'
    elif mac or name or func_1 or func_2 or func_3 or func_off or ip is None:
        return 'Error, Argument missing! \n Check this!'


#--------------------------------------------Del remote----------------------------------------#
@app.route('/del_remote', methods=['GET'])
def del_remote():
    key = request.args.get('keys')
    with open(access_remote, "r") as f:
        remote = json.load(f)
    if key in remote.keys():
        delremote(key)
        return 'Ok, remote was deleted with mac ' + key +'.'
    if key not in remote.keys():
        return 'This remote not existe!'
    else:
        return 'Error! Check argument.'


#--------------------------------------------Button----------------------------------------#
@app.route('/button', methods = ['GET'])
def button():
    status = request.args.get('stat')
    mac = request.args.get('mac')
    num = remotenum()
    with open(access_remote, "r") as f:
        remote = json.load(f)
    with open(access_user, "r") as f:
        user = json.load(f)
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
    app.run(port=3030, host='0.0.0.0', debug=True)


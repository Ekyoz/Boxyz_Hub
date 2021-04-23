from flask import Flask, request, render_template, session, redirect
import requests
import json
from remote import *

app = Flask(__name__)
url="http://192.168.1.29:3000/assistant"


#--------------------------------------------Home----------------------------------------#
@app.route('/add_remote', methods = ['GET'])
def add_remote():
    mac = request.args.get('mac')
    name = request.args.get('name')
    func = request.args.get('func')
    ip = request.args.get('ip')
    add_remote(mac=mac, name=name, func=func, ip=ip)
    return 'ok'


@app.route('/del_remote', methods=['GET'])
def del_remote():
    keys = request.args.get('keys')
    del_remote(keys=keys)


@app.route('/button', methods = ['GET','POST'])
def button():
    status = request.args.get('stat')
    ip = request.args.get('mac')
    requests.post(url=url, data=remote)



if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)


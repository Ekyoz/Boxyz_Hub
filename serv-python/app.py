from flask import Flask, request, render_template, session, redirect
import requests
import json
import remote

app = Flask(__name__)
url="http://192.168.1.29:3000/assistant"


#--------------------------------------------Home----------------------------------------#
@app.route('/add_remote', methods = ['GET'])
def add_remote():
    mac = str(request.args.get('mac'))
    name = str(request.args.get('name'))
    func = str(request.args.get('func'))
    ip = str(request.args.get('ip'))
    add_remote(mac, name, func, ip)



@app.route('/button', methods = ['GET','POST'])
def button():
    status = request.args.get('stat')
    ip = request.args.get('mac')
    requests.post(url=url, data=remote)



if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)


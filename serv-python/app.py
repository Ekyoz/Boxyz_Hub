from os import removedirs
from flask import Flask, request, render_template, session, redirect
import requests
import json

app = Flask(__name__)
remote_num =  []

file = open("/home/pi/Boxyz/serv-python/remote.json", "r")
remote = json.load(file)
for num in remote.keys():
    remote_num.append(num)

remote["bc:dd:c2:55:63"] = {"name" : "test", "func" : "test", "ip" : "192.168.1.25"}
json.dumps(remote)
file.close()

print(remote)

url="http://192.168.1.29:3000/assistant"


#--------------------------------------------Home----------------------------------------#
@app.route('/add_remote', methods = ['GET'])
def add_remote():
    mac = request.args.get('mac')
    name = request.args.get('name')
    func = request.args.get('func')
    ip = request.args.get('ip')


@app.route('/button', methods = ['GET','POST'])
def button():
    status = request.args.get('stat')
    ip = request.args.get('mac')
    requests.post(url=url, data=remote)



if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)


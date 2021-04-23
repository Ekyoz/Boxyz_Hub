from os import removedirs
from flask import Flask, request, render_template, session, redirect
import requests
import json

app = Flask(__name__)
remote_num =  []

remote = json.load(open("/home/pi/Boxyz/serv-python/remote.json", "r"))
for num in remote.keys():
    remote_num.append(num)
    print(remote_num)




url="http://192.168.1.29:3000/assistant"


#--------------------------------------------Home----------------------------------------#
@app.route('/button', methods = ['GET','POST'])
def button():
    status = request.args.get('stat')
    ip = request.args.get('mac')
    requests.post(url=url, data=remote)



if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)


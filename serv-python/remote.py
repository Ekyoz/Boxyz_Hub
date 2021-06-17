import json
from os import access

access_remote = "remote.json"
access_user = "../assistant-relay/bin/config.json"
remote_num =  []
url="http://localhost:3000/assistant"


def remotenum():
    remote_num =  []
    with open(access_remote, "r") as f:
        remote = json.load(f)
    for num in remote.keys():
        remote_num.append(num)
    return remote_num

def addremote(mac, name, func_on, func_off, ip):
    with open(access_remote, "r") as f:
        remote = json.load(f)
    with open(access_remote, "w") as f:
        remote[mac] = {"name" : str(name), "func_on" : str(func_on),"func_off" : str(func_off) , "ip" : str(ip)}
        json.dump(remote, f, indent=6)

def delremote(keys):
    with open(access_remote, "r") as f:
        remote = json.load(f)

    with open(access_remote, "w") as f:
        remote.pop(keys, None)
        json.dump(remote, f, indent=6)



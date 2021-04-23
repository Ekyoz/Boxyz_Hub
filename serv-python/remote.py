import json
from os import access

access = "../serv-python/remote.json"
remote_num =  []

def remotenum():
    with open(access, "r") as f:
        remote = json.load(f)
    remote_num =  []
    for num in remote.keys():
        remote_num.append(num)
    return remote_num



def addremote(mac, name, func, ip):
    with open(access, "r") as f:
        remote = json.load(f)

    with open(access, "w") as f:
        remote[mac] = {"name" : str(name), "func" : str(func), "ip" : str(ip)}
        json.dump(remote, f, indent=6)


def delremote(keys):
    with open(access, "r") as f:
        remote = json.load(f)

    with open(access, "w") as f:
        remote.pop(keys, None)
        json.dump(remote, f, indent=6)


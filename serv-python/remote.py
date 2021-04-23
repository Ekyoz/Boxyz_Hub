import json
from os import access

access = "../serv-python/remote.json"

def remote_info(info=None):
    remote_num =  []
    with open(access, "r") as f:
        remote = json.load(f)
    for num in remote.keys():
        remote_num.append(num)
    if info == num:
        print(remote_num)
    if info == json:
        print(remote)
    elif info == None:
        print(remote, remote_num)

def addremote(mac, name, func, ip):
    with open(access, "r") as f:
        remote = json.load(f)

    with open(access, "w") as f:
        remote[mac] = {"name" : str(name), "func" : str(func), "ip" : str(ip)}
        remote.pop("bc:dd:c2:55:63", None)
        json.dump(remote, f, indent=6)


def delremote(keys):
    with open(access, "r") as f:
        remote = json.load(f)

    with open(access, "w") as f:
        remote.pop(keys, None)
        json.dump(remote, f, indent=6)

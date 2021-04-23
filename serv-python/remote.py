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


def addremote(mac, name, func_on, func_off, ip):
    with open(access, "r") as f:
        remote = json.load(f)
    if mac and name and func_on and func_off and ip is not None:
        with open(access, "w") as f:
            remote[mac] = {"name" : str(name), "func_on" : str(func_on),"func_off" : str(func_off) , "ip" : str(ip)}
            json.dump(remote, f, indent=6)
    elif mac or name or func_on or func_off or ip is None:
        return 'Error!'


def delremote(keys):
    with open(access, "r") as f:
        remote = json.load(f)

    with open(access, "w") as f:
        remote.pop(keys, None)
        json.dump(remote, f, indent=6)


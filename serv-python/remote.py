import json
from os import access

access = "serv-python/remote.json"

def remote_num():
    remote_num =  []
    with open(access, "r") as f:
        remote = json.load(f)
    for num in remote.keys():
        remote_num.append(num)
    return remote_num

def add_remote(mac, name, func, ip):
    with open(access, "r") as f:
        remote = json.load(f)

    with open(access, "w") as f:
        try:
            remote[mac] = {"name" : str(name), "func" : str(func), "ip" : str(ip)}
            remote.pop("bc:dd:c2:55:63", None)
            json.dump(remote, f, indent=6)
            return "ok"
        except:
            return "argument missing or invalid"


def del_remote(keys):
    with open(access, "r") as f:
        remote = json.load(f)

    with open(access, "w") as f:
        remote.pop(keys, None)
        json.dump(remote, f, indent=6)


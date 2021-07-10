import json

access_rooms = "rooms.json"
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

def addremote(id_room, id_remote, mac, name, on_1, on_2, on_3, off):
    with open(access_rooms, "r") as f:
        rooms = json.load(f)
    with open(access_rooms, "w") as f:
        rooms[id_room]["remote"] = {str(id_room + "-" + id_remote + "R"):{"mac":str(mac),"name":str(name),"func":{"on-1":str(on_1),"on-2":str(on_2),"on-3":str(on_3),"off":str(off)}}}
        json.dump(rooms, f, indent=6)

def delremote(keys):
    with open(access_remote, "r") as f:
        remote = json.load(f)

    with open(access_remote, "w") as f:
        remote.pop(keys, None)
        json.dump(remote, f, indent=6)

addremote(id_room="02R", id_remote="03", mac="D8:BF:C0:14:test", name="test", on_1="test1", on_2="test2", on_3="test3", off="off")
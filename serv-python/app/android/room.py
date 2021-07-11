from flask import Blueprint, request
import json
import os

base_dir = "/home/pi/Documents/Boxyz/serv-python/app/json/"
jsonFile = "room.json"
access_rooms = os.path.join(base_dir,jsonFile)
AppRoom = Blueprint('room', __name__)

#-------Function-------#


def getRooms():
    with open(access_rooms, "r") as f:
        Json = json.load(f)
    for i in Json["rooms"]:
        return i[0:2]

def testComponent(IdRoom, Component):
    with open(access_rooms, "r") as f:
        rooms = json.load(f)
    compt = 1
    if IdRoom <= getRooms():
        if Component == "remote":
            try:
                while len(rooms["rooms"][IdRoom][Component]) != str("0" + str(compt)):
                    if rooms["rooms"][IdRoom][Component][IdRoom + "-0" + str(compt) + "R"] == None:
                        Id = str("0" + str(compt))
                        compt = len(rooms["rooms"][IdRoom][Component])
                        return Id
                    else:
                        compt += 1
            except:
                return "no empty component"
        if Component == "light":
            try:
                while len(rooms["rooms"][IdRoom][Component]) != str("0" + str(compt)):
                    if rooms["rooms"][IdRoom][Component][IdRoom + "-0" + str(compt) + "L"] == None:
                        Id = str("0" + str(compt))
                        compt = len(rooms["rooms"][IdRoom][Component])
                        return Id
                    else:
                        compt += 1
            except:
                return "no empty component"
        if Component == "accessories":
            try:
                while len(rooms["rooms"][IdRoom][Component]) != str("0" + str(compt)):
                    if rooms["rooms"][IdRoom][Component][IdRoom + "-0" + str(compt) + "A"] == None:
                        Id = str("0" + str(compt))
                        compt = len(rooms["rooms"][IdRoom][Component])
                        return Id
                    else:
                        compt += 1
            except:
                return "no empty component"
        else:
            return "Component not exist"
    else:
        return "Rooms not exist"

def getId(IdRoom, Component, Info):
    with open(access_rooms, "r") as f:
        Json = json.load(f)
    if IdRoom <= getRooms():
        if Component == "remote":
            if Info == "id":
                try:
                    for i in Json["rooms"][IdRoom][Component]:
                        remote = i[3:5]
                    return remote
                except:
                    return "There's no remote"
            if Info == "list":
                try:
                    for l in Json["rooms"][IdRoom][Component]:
                        List = list(Json["rooms"][IdRoom][Component].keys())
                    return List
                except:
                    return "There's no remote"
            else:
                return "Info don't exist or are wrong!"
        if Component == "light":
            if Info == "id":
                try:
                    for i in Json["rooms"][IdRoom][Component]:
                        remote = i[3:5]
                    return remote
                except:
                    return "There's no light"
            if Info == "list":
                try:
                    for l in Json["rooms"][IdRoom][Component]:
                        List = list(Json["rooms"][IdRoom][Component].keys())
                    return List
                except:
                    return "There's no light"
            else:
                return "Info don't exist or are wrong!"
        if Component == "accessories":
            if Info == "id":
                try:
                    for i in Json["rooms"][IdRoom][Component]:
                        remote = i[3:5]
                    return remote
                except:
                    return "There's no accessories"
            if Info == "list":
                try:
                    for l in Json["rooms"][IdRoom][Component]:
                        List = list(Json["rooms"][IdRoom][Component].keys())
                    return List
                except:
                    return "There's no accessories"
            else:
                return "Info don't exist or are wrong!"
        else:
            return "Component not exist!"
    else:
        return "Rooms not exist"

#-------Route-------#

@AppRoom.route("/", methods=["GET"])
def home():
    return "home room"

@AppRoom.route("/add", methods=['GET'])
def add():
    IdRoom = request.args.get('idroom')
    Component = request.args.get('component')
    if IdRoom and Component is not None:
        with open(access_rooms, "r") as f:
            rooms = json.load(f)
        if IdRoom <= getRooms():
            if Component == "remote":
                if getId(IdRoom, Component, "id") != "There's no remote":
                    if testComponent(IdRoom, Component) == "no empty component":
                        rooms["rooms"][IdRoom][Component][str(IdRoom + "-0" + str(int(getId(IdRoom, Component, "id"))+1) + "R")] = {"mac":"","name":"","func":{"on-1":"","on-2":"","on-3":"","off":""}}
                        with open(access_rooms, "w") as f:
                                json.dump(rooms, f, indent=6)
                        return "Remote has created"
                    elif testComponent(IdRoom, Component) != "no empty component":
                        rooms["rooms"][IdRoom][Component][str(IdRoom) + "-" + str(testComponent(IdRoom, Component)) + "R"] = {"mac":"","name":"","func":{"on-1":"","on-2":"","on-3":"","off":""}}
                        with open(access_rooms, "w") as f:
                                json.dump(rooms, f, indent=6)
                        return "Remote has created"
                if getId(IdRoom, Component, "id") == "There's no remote":
                    rooms["rooms"][IdRoom][Component][str(IdRoom + "-01R")] = {"mac":"","name":"","func":{"on-1":"","on-2":"","on-3":"","off":""}}
                    with open(access_rooms, "w") as f:
                            json.dump(rooms, f, indent=6)
                    return "Remote has created"
                else:
                    return "Error!"
            if Component == "light":
                if getId(IdRoom, Component, "id") != "There's no light":
                    if testComponent(IdRoom, Component) == "no empty component":
                        rooms["rooms"][IdRoom][Component][str(IdRoom + "-0" + str(int(getId(IdRoom, Component, "id"))+1) + "L")] = {"name":"","func_on":"","func_off":""}
                        with open(access_rooms, "w") as f:
                                json.dump(rooms, f, indent=6)
                        return "Light has created"
                    elif testComponent(IdRoom, Component) != "no empty component":
                        rooms["rooms"][IdRoom][Component][str(IdRoom) + "-" + str(testComponent(IdRoom, Component)) + "L"] = {"name":"","func_on":"","func_off":""}
                        with open(access_rooms, "w") as f:
                                json.dump(rooms, f, indent=6)
                        return "Light has created"
                if getId(IdRoom, Component, "id") == "There's no light":
                    rooms["rooms"][IdRoom][Component][str(IdRoom + "-01L")] = {"name":"","func_on":"","func_off":""}
                    with open(access_rooms, "w") as f:
                            json.dump(rooms, f, indent=6)
                    return "Light has created"
                else:
                    return "Error!"
            if Component == "accessories":
                if getId(IdRoom, Component, "id") != "There's no accessories":
                    if testComponent(IdRoom, Component) == "no empty component":
                        rooms["rooms"][IdRoom][Component][str(IdRoom + "-0" + str(int(getId(IdRoom, Component, "id"))+1) + "A")] = {"name":"","assistant":""}
                        with open(access_rooms, "w") as f:
                                json.dump(rooms, f, indent=6)
                        return "Accessories has created"
                    elif testComponent(IdRoom, Component) != "no empty component":
                        rooms["rooms"][IdRoom][Component][str(IdRoom) + "-" + str(testComponent(IdRoom, Component)) + "A"] = {"name":"","assistant":""}
                        with open(access_rooms, "w") as f:
                                json.dump(rooms, f, indent=6)
                        return "Accessories has created"
                if getId(IdRoom, Component, "id") == "There's no accessories":
                    rooms["rooms"][IdRoom][Component][str(IdRoom + "-01A")] = {"name":"","assistant":""}
                    with open(access_rooms, "w") as f:
                            json.dump(rooms, f, indent=6)
                    return "Accessories has created"
                else:
                    return "Error!"
            else:
                return("Component not exist")
        else:
            return "Room not exitst"
    else:
        return "Argument missing"

@AppRoom.route("/supp", methods=['GET'])
def supp():
    IdRoom = request.args.get('idroom')
    Component = request.args.get('component')
    Id = request.args.get('id')
    if IdRoom and Component and Id is not None:
        with open(access_rooms, "r") as f:
            rooms = json.load(f)
        if Component == "remote":
            if getId(IdRoom, Component, "list") == "There's no remote":
                return "Remote not exist"
            if int(Id) <= len(getId(IdRoom, Component, "list")):
                rooms["rooms"][IdRoom][Component][str(IdRoom) + "-" + str(Id) + "R"] = None
                with open(access_rooms, "w") as f:
                    json.dump(rooms, f, indent=6)
                return "Remote has delete"
            else:
                return "Remote not exist"
        if Component == "light":
            if getId(IdRoom, Component, "list") == "There's no light":
                return "Light not exist"
            if int(Id) <= len(getId(IdRoom, Component, "list")):
                rooms["rooms"][IdRoom][Component][str(IdRoom) + "-" + str(Id) + "L"] = None
                with open(access_rooms, "w") as f:
                    json.dump(rooms, f, indent=6)
                return "Light has delete"
            else:
                return "Remote not exist"
        if Component == "accessories":
            if getId(IdRoom, Component, "list") == "There's no accessories":
                return "accessories not exist"
            if int(Id) <= len(getId(IdRoom, Component, "list")):
                rooms["rooms"][IdRoom][Component][str(IdRoom) + "-" + str(Id) + "A"] = None
                with open(access_rooms, "w") as f:
                    json.dump(rooms, f, indent=6)
                return "Accessories has delete"
            else:
                return "Accessories not exist"
    else:
        return "Argument missing !"

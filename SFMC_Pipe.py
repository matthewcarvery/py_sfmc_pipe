import sys
from git import Repo
import os
import json

if __name__== "__main__":

    folder = sys.argv[1]
    BU = sys.argv[2]
 
    adds = json.loads(sys.argv[3])
    mods = json.loads(sys.argv[4])
    dels = json.loads(sys.argv[5])
    rens = json.loads(sys.argv[6].replace('\\"','\"'))
    type = json.loads(sys.argv[7])

    for x, item in enumerate(rens):
       pair = rens[x].split(',')
       dels.append(pair[0])
       adds.append(pair[1])

    print("Added: " + str(adds))
    print("Modifiied: " + str(mods))
    print("Deleted: " + str(dels) )
    print("Rename: " + str(rens))
    print("Type Change: " + str(type))

    f = open("main" + os.sep + adds[0], "r")
    print(f.read())

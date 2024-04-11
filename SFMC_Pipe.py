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
    ren1 = sys.argv[6]
    ren2 = ren1.replace('\\"','\"')
    rens = json.loads(ren2)
    type = json.loads(sys.argv[7])


    print("Added: " + sys.argv[3])
    print("Modifiied: " + sys.argv[4])
    print("Deleted: " + sys.argv[5]) 
    print("Rename: " + sys.argv[6])
    print("Type Change: " + sys.argv[7])

    print(rens[0].split(','))

    f = open("main" + os.sep + adds[0], "r")
    print(f.read())

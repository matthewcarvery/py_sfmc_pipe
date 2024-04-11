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
    rens = json.loads(sys.argv[6])
    type = json.loads(sys.argv[7])


    print("Added: " + adds)
    print("Modifiied: " + mods)
    print("Deleted: " + dels)
    print("Renamed: " + rens)
    print("Type Change: " + type)



    f = open("main" + os.sep + mods[0], "r")
    print(f.read())

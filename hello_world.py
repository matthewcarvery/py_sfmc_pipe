import sys
from git import Repo
import os
import json

if __name__== "__main__":
    print ('folder : ', sys.argv[1])
    print ('BU : ', sys.argv[2])
    print ('Adds : ', sys.argv[3])
    print ('Mods : ', sys.argv[4])
    print ('Dels : ', sys.argv[5])
    print ('Renames : ', sys.argv[6])
    print ('TypeChange : ', sys.argv[7])
    mods = json.loads(sys.argv[4])

    f = open("main" + mods[0], "r")
    print(f.read())

    print("Hi there!")
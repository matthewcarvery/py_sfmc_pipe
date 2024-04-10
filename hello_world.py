import sys
from git import Repo
import os

if __name__== "__main__":
    print ('folder : ', sys.argv[1])
    print ('BU : ', sys.argv[2])
    print ('Adds : ', sys.argv[3])
    print ('Mods : ', sys.argv[4])
    print ('Dels : ', sys.argv[5])
    print ('Renames : ', sys.argv[6])
    print ('TypeChange : ', sys.argv[7])

    f = open("main/test.htm", "r")
    print(f.read())

    print("Hi there!")
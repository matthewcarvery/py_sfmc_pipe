import sys
from git import Repo
import os

if __name__== "__main__":
    print ('folder : ', sys.argv[1])
    print ('BU : ', sys.argv[2])
    print ('Changes : ', sys.argv[3])

    f = open("main/test.htm", "r")
    print(f.read())

    print("Hi there!")
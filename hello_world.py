import sys

if __name__== "__main__":
    print ('folder : ', sys.argv[1])
    print ('BU : ', sys.argv[2])

    f = open("main/test.htm", "r")
    print(f.read())

    print("Hello World from the Devops repo!")
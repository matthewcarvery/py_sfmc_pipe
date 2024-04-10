import sys
from git import Repo
import os

if __name__== "__main__":
    print ('folder : ', sys.argv[1])
    print ('BU : ', sys.argv[2])

    f = open("main/test.htm", "r")
    print(f.read())

    print("Hello World!")
    
    def git_push(repofolder):
        try:
            modifiedFiles = []
            deletedFiles = []
            addedFiles = []
            repo = Repo(repofolder, search_parent_directories=True)
            git_root = repo.git.rev_parse("--show-toplevel")       
            previous_commit = repo.commit('HEAD~1')
            print(previous_commit.diff('HEAD'))
            '''
            for item in previous_commit.diff('HEAD'):
                match item.change_type:
                    case 'M':
                        modifiedFiles.append(os.path.normpath(os.path.join(git_root, item.a_path)))
                    case 'A':
                        addedFiles.append(os.path.normpath(os.path.join(git_root, item.a_path)))
                    case 'D':
                        deletedFiles.append(os.path.normpath(os.path.join(git_root, item.a_path)))
                    case 'R'|'T':
                        deletedFiles.append(os.path.normpath(os.path.join(git_root, item.a_path)))
                        addedFiles.append(os.path.normpath(os.path.join(git_root, item.b_path)))
            return(addedFiles, modifiedFiles, deletedFiles)
            '''
        except:
            print('Some error occured while pushing the code')   
        
    addedFiles, modifiedFiles, deletedFiles = git_push('main')
    print(modifiedFiles)
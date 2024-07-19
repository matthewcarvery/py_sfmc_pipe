import sys
import os
import json
import base64
import requests
from pathlib import Path
from assetlist import assets
from auth import generate_access_token
from plb import buildpayload

if __name__== "__main__":

   Refresh = False
   folderlist = []
   childfolders = []
   '''
   client_id = secret.account[accountname]['client_id']
   subdomain = secret.account[accountname]['subdomain']
   clientsecret = secret.account[accountname]['clientsecret']
   resturl = f'https://{subdomain}.rest.marketingcloudapis.com/'
   '''
   client_id = ""
   subdomain = ""
   clientsecret = ""
   resturl = ""

   repofolder = "main" + os.sep
   accountname = sys.argv[2]
   allfiles = json.loads(sys.argv[1])
   for x, item in enumerate(allfiles):
      pathlist = os.path.split(os.path.abspath(Path(allfiles[x])))
   print(pathlist)
   print(os.listdir(repofolder))

   '''
   cur_dir = sys.argv[7]
   file_name = "Project.yml"
   while True:
    file_list = os.listdir(cur_dir)
    parent_dir = os.path.dirname(cur_dir)
    if file_name in file_list:
        print("File Exists in: ", cur_dir)
        break
    else:
        if cur_dir == parent_dir: #if dir is root dir
            print("File not found")
            break
        else:
            cur_dir = parent_dir   
   '''
   masterfolder = 0
   addedFiles = json.loads(sys.argv[3])
   modifiedFiles = json.loads(sys.argv[4])
   deletedFiles = json.loads(sys.argv[5])
   rens = json.loads(sys.argv[6].replace('\\"','\"'))
   type = json.loads(sys.argv[7])

   for x, item in enumerate(rens):
      pair = rens[x].split(',')
      deletedFiles.append(pair[0])
      addedFiles.append(pair[1])

      #f = open("main" + os.sep + adds[0], "r")
      #print(f.read())

   def verifyfolder(pfolderid):
      print("Checking folder structure in SFMC")
      '''
      headers = {'authorization': f'Bearer {access_token}', 'content-type': 'application/json'}
      rest_url = f'{resturl}/asset/v1/content/categories?$page=1&$pagesize=10&$orderBy=name desc&$filter=parentId eq {pfolderid}'
      verify_request = requests.get(url=f'{rest_url}', headers=headers)
      refold = json.loads(verify_request.content)
      if refold['count'] > 0:
         for q in range(len(refold['items'])): 
               newid = {'id':refold['items'][q]['id'], 'name': refold['items'][q]['name'], 'parent': refold['items'][q]['parentId']}
               childfolders.append(newid)
               verifyfolder(refold['items'][q]['id'])
      '''         
        

   def delete_content(deletedFiles):
      deletablefiles = getdelete(deletedFiles)
      print("deleting " + str(deletedFiles) + " from SFMC" )
      '''
      headers = {'authorization': f'Bearer {access_token}', 'content-type': 'application/json'}
      for q in range(len(deletablefiles)):
         data, filename, filedir = definefile(deletablefiles[q], "del")
         insert_request = delete_assets(data, headers, filename, filedir)
         print("Deleting: " + filename) 
         print(insert_request)
      ''' 

   def getdelete(delete):
      print("Finding file locations for deletion in SFMC")
      '''
      r = []
      for q in delete:
         dirs = []
         folder = masterfolder
         dir = os.path.dirname(q)
         while os.path.normpath(repofolder) != dir:
               dirs.append(os.path.basename(dir))
               dir = os.path.dirname(dir)
         dirs.reverse()
         for x in range(len(dirs)):
               folderids = [item for item in childfolders if item.get('name') == dirs[x] and item.get('parent') == folder]
               if len(folderids) > 0:
                  folder = folderids[0]['id']
         r.append ({'file':os.path.normpath(q), 'dir':folder})
      return(r)
      '''
   

   def import_content(filelist, addedFiles, modifiedFiles):
      print("Finding and adding " + str(addedFiles))
      print("Finding and updating " + str(modifiedFiles))
      '''
      headers = {'authorization': f'Bearer {access_token}', 'content-type': 'application/json'}
      for x in range(len(filelist)):
         data, filename, filedir = definefile(filelist[x], "add")
         if filelist[x]['file'] in addedFiles and Refresh == False:  
               insert_request = add_assets(data, headers)
         elif filelist[x]['file'] in modifiedFiles or Refresh == True:
               check_url = f'{resturl}asset/v1/content/assets/?$filter=name = {filename} and category.id = {filedir}'
               check_request = requests.get(url=f'{check_url}', data=json.dumps(data), headers=headers)
               existcheck = json.loads(check_request.content)
               if existcheck['count'] > 0:  
                  patchid = existcheck['items'][0]['id']
                  insert_request = modify_assets(data, headers, patchid)
               else:
                  insert_request = add_assets(data, headers)
         else:
               insert_request = "File not changed. Skipping." 
         print(filename) 
         print(insert_request)
         ''' 

   def definefile(currentfile,type):
      filesplit, file_extension = os.path.splitext(currentfile['file'])
      file_ext = file_extension.translate({ord('.'): None})
      filedir = currentfile['dir']
      filename = os.path.basename(filesplit)
      assetparent = assets[file_ext]['parent']
      if type == "add":
         if assetparent in ('code', 'message', 'block'):
               with open(currentfile['file'], 'r') as f:
                  filecontent = f.read()
         else:
               with open(currentfile['file'], 'rb') as f:
                  filecontent = base64.b64encode(f.read()).decode('utf-8')
      else:
         filecontent = ""     
      data = buildpayload(filename, file_ext, filecontent, filedir, masterfolder)
      data = {"file": "data"}
      return(data, filename, filedir) 


   def modify_assets(data, headers, patchid):
      rest_url = f'{resturl}/asset/v1/content/assets/{patchid}'
      insert_request = requests.patch(url=f'{rest_url}', data=json.dumps(data), headers=headers)   
      return(insert_request)

   def add_assets(data, headers):
      rest_url = f'{resturl}/asset/v1/content/assets/'
      insert_request = requests.post(url=f'{rest_url}', data=json.dumps(data), headers=headers)
      return(insert_request)

   def delete_assets(data, headers, filename, filedir):
      check_url = f'{resturl}asset/v1/content/assets/?$filter=name = {filename} and category.id = {filedir}'
      check_request = requests.get(url=f'{check_url}', data=json.dumps(data), headers=headers)
      existcheck = json.loads(check_request.content)
      if len(existcheck['items']) > 0:
         delid = existcheck['items'][0]['id']
         rest_url = f'{resturl}/asset/v1/content/assets/{delid}'
         insert_request = requests.delete(url=f'{rest_url}', data=json.dumps(data), headers=headers)
      else: 
         insert_request = "File to be Deleted not found"   
      return(insert_request)                

   def list_files(dir):
    print('Matching folder paths to SFMC category ids')
    '''
    r = []
    exclude = set(['New folder', 'Windows', 'Desktop', '.git'])
    skip = ('.md', '.yml')
    for root, dirs, files in os.walk(dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        files[:] = [f for f in files if not f.endswith(skip)]
        parentpath = os.path.dirname(root)
        if root != dir:
            if parentpath == dir:
                newid = [item for item in childfolders if item.get('name') == os.path.basename(root)]
                if len(newid) > 0:
                    newid[0]['path'] = root
                else:
                    makedir(os.path.basename(root), masterfolder, root)       
            else:
                parentid = [item for item in childfolders if item.get('path') == parentpath]
                newid = [item for item in childfolders if item.get('name') == os.path.basename(root) and item.get('parent') == parentid[0]['id']]
                if len(newid) > 0:
                    newid[0]['path'] = root
                else:
                    makedir(os.path.basename(root), parentid[0]['id'], root)    
        for name in files:
            if root != dir:
                newid = [item for item in childfolders if item.get('name') == os.path.basename(root) and item.get('path') == root]
                if len(newid) > 0:
                    folderid = newid[0]['id']
            else:
                folderid = masterfolder     
            r.append({'file':os.path.normpath(os.path.join(root, name)), 'dir':folderid})
    return r
    '''

   def makedir(dirname, parentdirid, dirpath):
    body = {
        "Name": dirname,
        "ParentId":parentdirid
    }
    headers = {'authorization': f'Bearer {access_token}', 'content-type': 'application/json'}
    rest_url = f'{resturl}/asset/v1/content/categories'
    folder_request = requests.post(url=f'{rest_url}', data=json.dumps(body), headers=headers)
    foldercreate = json.loads(folder_request.content)
    childfolders.append({'id':foldercreate['id'],'name':dirname, 'parent':parentdirid, 'path': dirpath})


   access_token = generate_access_token(client_id, clientsecret, subdomain)
   verifyfolder(masterfolder)
   #delete_content(deletedFiles)
   filelist = list_files(repofolder)
   #import_content(filelist, addedFiles, modifiedFiles)

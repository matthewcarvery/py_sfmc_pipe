from assetlist import assets

def buildpayload(filename, file_ext, filecontent, filedir, masterdir):
    assetId = assets[file_ext]['id']
    assetname = assets[file_ext]['desc']
    assetparent = assets[file_ext]['parent']
    print(assetparent)      
    match assetparent:
        case "code" | "message" | "block" :
            match file_ext:    
                case "htmlemail":
                    print(assetId)      
                    jobj= {"name": filename,
                        "channels": {
                            "email": True,
                            "web": False
                        },
                        "views": {
                            "html": {
                                "content": filecontent
                                },
                            "text": {},
                            "subjectline": {
                                "content": "%%=v(@subject_line)=%%"
                            },
                            "preheader": {
                                "content": "%%=v(@preheader)=%%"
                            }
                        },
                        "assetType": {
                            "name": assetname,
                            "id": assetId
                        },
                        "category": { "id": filedir },
                        "customerkey": filename + "_" + str(masterdir)
                    }
                case other:            
                    jobj= {"name": filename,
                        "channels": {
                            "email": True,
                            "web": True
                        },
                        "content": filecontent,
                        "assetType": {
                            "name": assetname,
                            "id": assetId
                        },
                        "category": { "id": filedir },
                        "customerkey": filename + "_" + str(masterdir)
                    }
        case other:
                      jobj= {"name": filename,
                        "channels": {
                            "email": True,
                            "web": True
                        },
                        "FileProperties": {
                            "fileName": f'{filename}.{file_ext}'
                        },
                        "file":  filecontent,
                        "assetType": {
                            "name": assetname,
                            "id": assetId
                        },
                        "category": { "id": filedir },
                        "customerkey": filename + "_" + str(masterdir)
                    } 
    return(jobj)       
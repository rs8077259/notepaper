import hashlib

def fileSha26Hash(fileObject:open):
    hash=hashlib.sha256()#calculating SHA checksum of transfered file 
    while(chunck:=fileObject.read(5400)):
        hash.update(chunck)
    return hash.hexdigest()

def isMarkDownFile(filename:str)->str:
    if filename[-3:]=='.md':
        return True
    return False

def replaceMarkdownFile(tableObject,file:open,hash:str):
    try:
        tableObject.file.delete(save=False)# deleting previous file
        tableObject.file=file
        tableObject.hash=hash
        tableObject.save()
        return True
    except:
        return False


def replaceMediaFile(tableObject,file:open,hash:str):
    try:
        tableObject.file.delete(save=False)# deleting previous file
        tableObject.file=file
        tableObject.hash=hash
        tableObject.save()
        return True
    except:
        return False
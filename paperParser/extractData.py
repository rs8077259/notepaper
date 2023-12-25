import os
import re
class MD:
    def __init__(self,filename:str=None):
        if filename:
            file=open(filename)
            filer=file.read()
            self.poster(filer)
            self.fileName=file.name.split('/')[-1][:-3]
            self.title(file,filer)
            file.close()

        else:
            file=''
    def open(self,fileDir:str):
        file=open(fileDir)
        filer=file.read()
        self.title(file,filer)
        file.close()
    def file(self,file:str):
        filer=file.read()
        self.fileName=file.name.split('/')[-1][:-3]
        self.title(file,filer)


    def title(self,fileobj:open,file:str):
        title=re.findall('^# (.*)',str(file) )
        if title:
            self.Title=title[0] 
            
        else:
            self.Title=fileobj.name.split('/')[-1][:-3]
        return self.Title

    def h2(self,fileobj:open,file:str):
        title=re.findall('^## (.*)',file)
        if title:
            self.H2=title
            return self.H2
    def isImg(self,text:str)->bool:
        return True if text.split('.')[-1] in ('jpeg','jpg','tiff','bmp','png','gif','psd','ai','raw','svg') else False
    def h3(self,file:str):
        title=re.findall('^### (.*)',file)
        if title:
            self.H3=title
            return self.H3

    def h4(self,file:str):
        title=re.findall('^#### (.*)',file)
        if title:
            self.H4=title
            return self.H4

    def h5(self,file:str):
        title=re.findall('^##### (.*)',file)
        if title:
            self.H5=title
            return self.H5

    def h6(self,file:str):
        title=re.findall('^###### (.*)',file)
        if title:
            self.H6=title
            return self.H6

    def poster(self,file:str=''):
        #extract poster image of file
        if poster:=re.findall('^poster=\[\[(.*)\]\]',file):
            self.Poster=poster
        elif poster:=re.findall('!\[\[(.*)\]\]',file):
            for text in poster:
                if self.isImg(text):
                    self.Poster=poster[0].replace(' ','_').replace('~','')
                    break
                else:
                    self.Poster=''
        else:
            self.Poster=''

    def tags(self,text):
        #to be defined
        pass
    
    


from django.shortcuts import render
from django.template import loader
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PaperModel,MediaModel,NoteData
from paperParser.html import Html
from paperParser.extractData import MD
from threading import Thread
import json
import hashlib
from django.urls import reverse
import os
@api_view(['POST'])
def recivefile(request):
    '''this function receive file uploaded from client side
    assuming file as list of touples where first element of list contains <file name> and secound argument contains <binary of file>:-
        [ (file_name,binary) ]
        
    it first casculate SHA256 checksum of file sent used to distinguish when file is modified and then save SHA and file '''
    for names in request.FILES:  # ther could be multiple file in request And request.Files return dictionary for the format {'filename':binary}
        if names[-3:]=='.md':
            #savinf markdown file
            
            hash=hashlib.sha256()#calculating SHA checksum of transfered file 
            file=request.FILES[names]
            while(chunck:=file.read(5400)):
                hash.update(chunck)
            hash=hash.hexdigest()

            try:
                # checkin file of same name exists 
                filedb=PaperModel.objects.get(filename=names)
                what = filedb.hash == hash # checking sha hash of file to determine wether file is modified
                if what==False:
                    filedb.file.delete(save=False)# deleting previous file
                    filedb.file=request.FILES[names]
                    filedb.hash=hash
                    filedb.save()
                
            except:
                form=PaperModel(names,request.FILES[names],hash)
                form.save()
            location=PaperModel.objects.get(filename=names).file
            obj=MD(os.getcwd()+'/'+str(location))
            NoteData(obj.fileName,obj.Title,obj.Poster).save()
        else:
            #for saving media files image,video
            hash=hashlib.sha256()
            file=request.FILES[names]
            while(chunck:=file.read(5400)):
                hash.update(chunck)
            hash=hash.hexdigest()
            try:
                # checkin file of same name exists 
                filedb=MediaModel.objects.get(filename=names)
                
                what = filedb.hash == hash
                if what==False:
                    filedb.file.delete(save=False)# deleting previous file
                    filedb.file=request.FILES[names]
                    filedb.hash=hash
                    filedb.save()
                
            except:
                form=MediaModel(names,request.FILES[names],hash)
                form.save()
            
            
    return Response({'status':'created'},status=status.HTTP_201_CREATED)

@api_view(['GET'])
def sendfile(request,pagename):
    '''
    sends viewable file to user 
    '''
    try:
        location=PaperModel.objects.get(filename=pagename+'.md').file
    except:
        return Response({'status':404,'detail':"file not found"},status=status.HTTP_404_NOT_FOUND)
    html=Html(os.getcwd()+'/'+str(location))
    html.convertToHtml()
    context={'html':html.html,'title':html.Title}
    return render(request,'page.html',context=context)
    
@api_view(['POST'])
def checkfile(request):
    '''check wheather the file exist or is modified if modified or not found it sends file name to client'''
    responseJson={'file':[]}
    file=json.loads(request.data)
    for key in file:
        if key.split('.')[-1]=='md':
            #check wearher md file exists,to be modified,doesnot exist
            try:
                filedb=PaperModel.objects.get(filename=key.replace(' ',''))#removing spaces from file so because the space are removed when strings are stored in db
                if filedb.hash!=file[key]:
                    responseJson['file'].append(key)
            except Exception as E:
                responseJson['file'].append(key)

        else:
            try:
                filedb=MediaModel.objects.get(filename=key.replace(' ',''))#removing spaces from file so because the space are removed when strings are stored in db
                if filedb.hash!=file[key]:
                    responseJson['file'].append(key)   
            except:
                responseJson['file'].append(key)
    return Response(responseJson,status=status.HTTP_200_OK)

    


    
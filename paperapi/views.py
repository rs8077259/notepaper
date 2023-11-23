from django.shortcuts import render
from django.template import loader
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PaperModel,MediaModel
from paperParser.html import Html
from threading import Thread
import json
from django.urls import reverse
import os

@api_view(['POST'])
def recivefile(request):
    '''this function receive file uploaded from client side
    assuming file as list of touples where first element of list contains <file name> and secound argument contains <binary of file>:-
        [ (file_name,binary) ]'''
    for names in request.FILES:  # ther could be multiple file in request And request.Files return dictionary for the format {'filename':binary}
        if names[-3:]=='.md':
            #savinf markdown file
            form=PaperModel(names,request.FILES[names])
            form.save()
        else:
            #for saving media files image,video
            form=MediaModel(names,request.FILES[names])
            form.save()
    return Response({'status':'ok'},status=status.HTTP_200_OK)

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
    print(html.Title)
    context={'html':html.html,'title':html.Title}
    return render(request,'page.html',context=context)
    
@api_view(['POST'])
def checkfile(request):
    responseJson={'file':[]}
    file=json.loads(request.data)
    for key in file:
        try:
            PaperModel.objects.get(filename=key)
        except:
            try:
                MediaModel.objects.get(filename=key)
            except:
                responseJson['file'].append(key)
    return Response(responseJson,status=status.HTTP_200_OK)

    



    

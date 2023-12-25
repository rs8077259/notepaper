from django.shortcuts import render
from paperapi.views import NoteData
from .serializers import NoteDataSerializers
from django.template import loader
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator,EmptyPage


@api_view(['GET'])
def getPaperData(request):
    perpage=request.GET.get('perpage',default=2)

    page=request.GET.get('page',default=1)
    data=NoteData.objects.all()
    paginator=Paginator(data,per_page=perpage)
    try:
        items=paginator.page(page)
    except EmptyPage:
        items=[]
    serializedItem=NoteDataSerializers(items,many=True)
    return Response(serializedItem.data)

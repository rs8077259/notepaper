from rest_framework import serializers
from django.urls import reverse
from django.templatetags.static import static
class NoteDataSerializers(serializers.Serializer):
    filename=serializers.CharField(max_length=70)
    title=serializers.CharField(max_length=100)
    pageImage=serializers.CharField(max_length=200)
    tags=serializers.CharField(max_length=70)
    url=serializers.SerializerMethodField(method_name='makeUrl')
    imgUrl=serializers.SerializerMethodField(method_name='imageUrl')
    def makeUrl(self,obj):
        if obj.filename:
            return reverse('paperapi:sendfile',args=[obj.filename])

    def imageUrl(self,obj):
        if obj.pageImage:
            return static('media/'+obj.pageImage)
        return ''
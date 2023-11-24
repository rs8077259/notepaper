from django.db import models
import datetime
import django
class PaperModel(models.Model):
    class Meta:
        db_table="paper"
    filename=models.CharField(max_length=250,primary_key=True)
    file=models.FileField(upload_to='md/',null=False,)
    hash=models.CharField(max_length=65,default=None,null=True)
    def __str__(self) -> str:
        return self.filename

class MediaModel(models.Model):
    class Meta:
        db_table="media"
    filename=models.CharField(max_length=255,primary_key=True)
    file=models.FileField(upload_to='paperapi/static/media')
    hash=models.CharField(max_length=65,default=None,null=True)
    def __str__(self) -> str:
        return self.filename
    
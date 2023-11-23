from django.db import models
import datetime
import django
class PaperModel(models.Model):
    class Meta:
        db_table="paper"
    filename=models.CharField(max_length=250,primary_key=True)
    file=models.FileField(upload_to='md/',null=False,)
    modifiedTime=models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self) -> str:
        return self.filename

class MediaModel(models.Model):
    filename=models.CharField(max_length=255,primary_key=True)
    file=models.FileField(upload_to='paperapi/static/media')
    modifiedTime=models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self) -> str:
        return self.filename
    class Meta:
        db_table="media"
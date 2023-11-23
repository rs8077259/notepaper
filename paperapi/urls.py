from django.urls import path
from . import views
app_name='paperapi'
urlpatterns=[
    path('file/push',views.recivefile,name='recivefile'),
    path("paper/get/<str:pagename>",views.sendfile,name='sendfile'),
    path("paper/check",views.checkfile,name='checkpaper'),
]
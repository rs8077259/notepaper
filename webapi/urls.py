from django.urls import path
from .views import getPaperData
urlpatterns=[
    path('note/',getPaperData,name='paperdata')
]
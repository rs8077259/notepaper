from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path("",include("website.urls")),
    path("admin/", admin.site.urls),
    path("api/",include("paperapi.urls")),
    path("error/",include("errorhandler.urls")),
    path('api/',include('webapi.urls'))
]

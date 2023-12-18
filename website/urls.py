from django.urls import path
from django.views.generic import TemplateView
from .views import HomePage
urlpatterns = [
    path("",HomePage),
    path('sw.js',TemplateView.as_view(template_name='app/sw.js',content_type='application/javascript'))
]
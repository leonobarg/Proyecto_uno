from django.urls import path
from . import views

urlpatterns = [
    path("family", views.flia),
    path("alta_flia/<nombre>,<fecha>,<edad>,<parentesco>", views.alta_flia)
]
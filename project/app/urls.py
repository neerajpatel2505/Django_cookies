from django.urls import path
from .views import *
# from .import views

urlpatterns = [
    path("set/",set,name="set"),
    path("get/",get,name="get"),
    path("delete/",delete,name="delete"),
]
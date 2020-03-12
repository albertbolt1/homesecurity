from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('/second', views.second, name='second'),
    path('/live', views.live, name='live1'),
    path('/face', views.facecrop, name='live2'),
    path('/facedetected', views.detectedfaces, name='live3'),
    path('/battery', views.battery, name='live4'),
    path('/proximity', views.proximity, name='live5'),
    path('/light', views.light, name='live6'),
    path('/home', views.home, name='home'),
    path('', views.home1, name='home1'),
    path('/home2', views.home2, name='home2'),
    path('/motion', views.motion, name='motion'),
    path('/missing', views.missing, name='missing'),
    path('/outof', views.outof, name='outof'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('main/', views.main, name='main'),
    path('test/', views.test, name='test'),
    path('killing-pop-music/', views.killingPopMusic, name='killing-pop-music'),
    # path('gallery/', views.gallery, name='gallery'),
]

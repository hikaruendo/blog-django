from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('bstest', views.bstest, name='bstest'),
    path('exercise', views.exercise, name='exercise'),
    path('loop', views.loop, name='loop'),
    path('query', views.query, name='query'),
]
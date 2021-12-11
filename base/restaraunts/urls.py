from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaraunts, name='restaraunts'),
    path('create/', views.create_restaraunt, name='restaraunt_create')
]

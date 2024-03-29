from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('book/<int:pk>', views.book, name='book'),
    path('confirm/<int:pk>/', views.confirm, name='confirm'),
]

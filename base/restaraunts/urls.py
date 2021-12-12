from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaraunts, name='restaraunts'),
    path('get_tables/<int:pk>', views.get_tables, name='get_tables'),
    path('create/', views.create_restaraunt, name='restaraunt_create'),
    path('update/<int:pk>/', views.update_restaraunt, name='restaraunt_update'),
    path('delete/<int:pk>/', views.delete_restaraunt, name='restaraunt_delete'),
]

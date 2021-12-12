from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaraunts, name='restaraunts'),

    path('waiter/', views.waiter, name='waiter'),
    path('menu/', views.show_menu, name='show_menu'),
    path('get_tables/<int:pk>', views.get_tables, name='get_tables'),
    path('get_free_time/<int:pk>', views.get_free_time, name='get_free_time'),
    path('get_end_time/<int:pk>/<int:chosen_time>', views.get_end_time, name='get_end_time'),
    path('create/', views.create_restaraunt, name='restaraunt_create'),
    path('update/<int:pk>/', views.update_restaraunt, name='restaraunt_update'),
    path('delete/<int:pk>/', views.delete_restaraunt, name='restaraunt_delete'),
]

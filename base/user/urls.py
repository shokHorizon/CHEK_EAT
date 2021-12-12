from django.urls import path
from . import views

urlpatterns = [
    path('crm/', views.crm, name='crm'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='index'),
]

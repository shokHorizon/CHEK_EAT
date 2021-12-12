from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('book.urls')),
    path('restaraunts/', include('restaraunts.urls')),
    path('', include('user.urls')),
]

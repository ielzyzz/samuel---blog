from django.contrib import admin
from django.urls import path,incluide

urlpatterns = [
    path('admin/', admin.site.urls),
  path ('', incluide('blog.urls')), 
]
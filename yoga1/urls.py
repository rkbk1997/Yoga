"""yoga1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from yoga.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('aboutview',aboutview,name='aboutview'),
    path('logout',Logout,name='logout'),
    path('main',main,name='main'),
    path('viewruetine',viewruetine,name='viewruetine'),
    path('login',Login,name='login'),
    path('timetable',timetable,name='timetable'),
    path('courses',courses,name='courses'),
    path('contact',contact,name='contact'),
    path('trainers',trainers,name='trainers'),
    path('schedule',schedule,name='schedule'),
    path('about',aboutpage,name='about'),
    path('index',indexpage,name='index'),
    path('admin/', admin.site.urls),
    path('^edit_delete_timetable/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',Edit_Delete_timetable,name="edit_delete_timetable"),
    path('^edit_delete_about/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',Edit_Delete_about,name="edit_delete_about"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
URL configuration for asrec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/',views.event, name='event'),
    path('about/',views.about, name='about'),
    path('',views.index, name='index'),
    path('login_admin/', login_admin, name='login_admin'),
    path('admin_home/', admin_home, name='admin_home'),
    path('logout/', Logout, name='logout'),
    path('admin_home/member/', views.member, name='member'),
    path('contact/', contact, name='contact'),
    path('admin_home/unread_queries/', views.unread_queries, name='unread_queires'),
    
    path('admin_home/read_queries/', views.read_queries, name='read_queires'),
    path('view_queries/<int:pid>', views.view_queries, name='view_queries'),
    path('admin_home/blog/', views.blog, name='blog'),
    
    path('viewblogs/', views.viewblogs, name='viewblogs'),
    path('displayblog/', views.displayblog, name="displayBlog"),
    path('teams/', views.teams, name='teams'),
    path('displayteam/',views.displayTeam, name='displayTeam'),

    path('training/', views.training, name='training'),
    path('view_training/', views.view_training, name='view_training'),
    path('displaytraining/', views.displayTrainings, name='displayTrainings'),

    path('admin_home/event',views.event_admin, name='event_admin'),
    path('view_event/', views.view_event, name='view_event'),
    path('displayevent/', views.displayEvent, name='displayEvent')
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""jobfair_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from jobfair_app import views

app_name = 'jobfair_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project_list/',views.ProjectListView.as_view(), name = 'project_list'),
    path('project_list/<pk>/',views.ProjectDetailView.as_view(), name = 'project_detail'),
    path('project_create/',views.ProjectCreateView.as_view(), name = 'project_create'),
    path('project_update/<pk>/',views.ProjectUpdateView.as_view(), name = 'project_update'),
    path('project_delete/<pk>/',views.ProjectDeleteView.as_view(), name = 'project_delete'),
    path('dashboard',views.dashboard, name = 'dashboard'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('login', views.user_login, name='user_login'),
]

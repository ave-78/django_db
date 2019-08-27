"""django_work URL Configuration

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
from django.urls import re_path, include
from django.views.generic import TemplateView
from main import views
from decor import views as decor_views

urlpatterns = [
    path('db_test/', include('db_test.urls')),
    path('decor/', decor_views.index),
    path('topic/<int:pk>/', decor_views.topic_details, name='topic_details'),
    path('', views.index, name='home'),
    path('create/', views.create),
    path('persons/', views.person),
    path('persons/edit/<int:id>/', views.edit),
    path('persons/delete/<int:id>/', views.delete),
    path('main', views.main),
    path('main1', views.main1),
    re_path(r'^about/?$', TemplateView.as_view(template_name="about.html")),
    path('contact/', TemplateView.as_view(template_name="main/contact.html")),
    path('details/', views.details),
    re_path(r'^products/?$', views.products),
    re_path(r'^users/?$', views.users),
    re_path('^products/(?P<product_id>\d+)/?', views.products),
    path('users/<int:id>/<str:name>', views.users),
    path('admin/', admin.site.urls),
]

from django.urls import path
from db_test import views

app_name = 'db_test'

urlpatterns = [
    path('create/user/', views.create_user, name='create_user'),
    path('create/blog/', views.create_blog, name='create_blog'),
    path('create/topic/', views.create_topic2, name='create_topic'),
    path('report/', views.report, name='report'),
    path('delete/user/<int:id>/', views.delete_user, name='delete_user'),
    path('delete/blog/<int:id>/', views.delete_blog, name = 'delete_blog'),
    path('delete/topic/<int:id>/', views.delete_topic, name = 'delete_topic'),
    path('subscribe/', views.subscribe_user, name='subscribe_user'),
    path('unsubscribe/', views.unsubscribe_user, name = 'unsubscribe_user'),
    path('like/', views.like, name='like_topic'),
    path('edit/users/', views.edit_users, name='edit_users')
]
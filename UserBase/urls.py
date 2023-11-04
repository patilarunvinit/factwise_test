from django.urls import path
from . import views

urlpatterns=[
    path('create_user/', views.create_user),
    path('list_users/', views.list_users),
    path('describe_user/', views.describe_user),
    path('update_user/', views.update_user),
    path('user_teams/', views.get_user_teams),

]
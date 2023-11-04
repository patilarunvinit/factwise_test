from django.urls import path
from . import views

urlpatterns=[
    path('create_team/', views.create_team),
    path('list_teams/', views.list_teams),
    path('describe_team/', views.describe_team),
    path('update_team/', views.update_team),
    path('add_users/', views.add_users_to_team),
    path('remove_users/', views.remove_users_from_team),
    path('team_users/', views.list_team_users),


]
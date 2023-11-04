from django.urls import path
from . import views

urlpatterns=[
    path('create_board/', views.create_board),
    path('close_board/', views.close_board),
    path('add_task/', views.add_task),
    path('task_status/', views.update_task_status),
    path('list_boards/', views.list_boards),
    path('export_board/', views.export_board),



]
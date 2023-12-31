from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_sheet/', views.add_sheet, name='add_sheet'),
    path('enter_number/', views.enter_number, name='enter_number'),
    path('new_game/', views.new_game, name='new_game'),
    path('delete_sheet/<int:sheet_id>/', views.delete_sheet, name='delete_sheet'),
]

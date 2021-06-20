from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('create', views.Add_new, name='add_new'),
    path('alldata', views.View_All, name='all_data'),
    path('searchdata', views.Search_data, name='searchdata'),

]

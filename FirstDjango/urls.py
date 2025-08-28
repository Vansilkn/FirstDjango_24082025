from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('items/<int:item_id>/', views.get_items),
]

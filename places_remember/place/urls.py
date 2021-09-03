from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_home, name='place-home'),
    path('list/', views.place_list, name='place-list'),
]

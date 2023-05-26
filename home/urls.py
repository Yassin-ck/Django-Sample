from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('offers',views.offers),
    path('contact',views.contact)
]

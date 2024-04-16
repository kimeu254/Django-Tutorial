from django.urls import path
from personal import views

urlpatterns = [
    path('', views.index, name='home'),
]
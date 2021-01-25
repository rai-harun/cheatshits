from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShitHome, name="shithome"),
    path('', views.CheatShitForView, name="cheatshitforview"),
]

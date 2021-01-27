from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShitHome, name="shithome"),
    path('shitfile/<int:pk>/', views.ShitDetails, name="shitdetails"),
]

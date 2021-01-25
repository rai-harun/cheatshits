from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShitHome, name="shithome"),
    # path('category/<int:pk>/', views.ShitHomeUrl, name="shithomeurl"),
]

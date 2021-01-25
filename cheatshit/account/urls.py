from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLogin, name="userlogin"),
    path('logout/', views.UserLogout, name="userlogout"),
    path('cheats/', views.UserView, name="userview"),

]

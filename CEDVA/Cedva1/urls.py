from django.urls import path
from Cedva1 import views

urlpatterns = [
    path('loginuser/',views.LoginUser, name="loginuser"),
    path('homepage',views.HomePage, name="homepage"),   
    path('logout/', views.LogoutUser, name="logout"), 
    path('clicklogin', views.clicklogin, name="clicklogin"),
    path('',views.LoginUser,name=""),    
]
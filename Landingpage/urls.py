from django.urls import path, include
from Landingpage import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.user_login,name='user_login'),
    path('logout',views.user_logout,name='user_logout'),
    path('register',views.register,name='register'),
    path('landing',views.landing,name='landing'),
]

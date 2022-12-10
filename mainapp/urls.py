from django.contrib import admin
from django.urls import path, include
from mainapp.views import frontpage, signup, login, profilepage
from django.contrib.auth import views


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='mainapp/login.html'), name='login'),
    path('profilepage/', profilepage, name='profilepage'),



]
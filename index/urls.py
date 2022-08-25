from django.urls import path
from .views import home, courses, register, login1, register_done, userspage, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('login1/', auth_views.LoginView.as_view(template_name='login1.html'), name='login1'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('register_done', register_done, name='register_done'),
    path('userspage/', userspage, name='userspage'),
]
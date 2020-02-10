from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('django.contrib.auth'))
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.logout, name='password_change'), 
]

 
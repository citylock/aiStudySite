from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'), 
    path('secret/', views.secret_page, name='secret'), 
    path('secret2/', views.SecretPage.as_view(), name='secret2'), 
]
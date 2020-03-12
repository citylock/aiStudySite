from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.quizList, name='quizList'),
    path('', views.QuizList.as_view(), name='quiz-list'), 
    path('<slug:slug>/', views.QuizDetail.as_view(), name='quiz-detail'), 
    path('<slug:slug>/test/', views.quizTest, name='quiz-test'), 
    # path('<slug:slug>/test/', views.quizTake, name='quiz-take'),     # version 1 
    # path('/taken/', views.quizTake, name='quizTaken')
    # path('<slug>/test/', views.quizTake, name='quizTake')
]
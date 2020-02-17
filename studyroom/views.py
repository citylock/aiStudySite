from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import FormView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Quiz, Question
from .forms import QuestionForm


# Create your views here.

def quizList(request):

    count = User.objects.count()
    quizzes = Quiz.objects.all()
    context = {
        'count': count, 
        'quizzes': quizzes
        }
    return render(request, 'studyroom/quiz-list.html', context )
    
class QuizList(ListView):
    model = Quiz
    template_name = 'studyroom/QuizList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



def quizDetail(request, slug):
    quiz = Quiz.objects.get(slug = slug)

    context = {
        'slug': slug,
        'quiz': quiz 
        }

    return render(request, 'studyroom/quizDetail.html', context )

class QuizDetail(DetailView):
    model = Quiz
    template_name = 'studyroom/QuizDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def quizTake(request, slug):
    print("===== Log IN :: view quizTake ===========")
    qquiz = Quiz.objects.filter(slug=slug)
    print(qquiz)
    questions = Question.objects.filter(pk=1)
    for question in questions: 
        print (question.pk,question.quiz)
    context = {}

    return render(request, 'studyroom/quizTake.html', context)
# class QuizTake(FormView):
#     print ("Log :: IN :: class QuizTake.. ")
#     form = QuestionForm
#     template_name = 'quizTake.html'
#     result_template_name = 'result.html'
#     single_complete_template_name = 'single_complete.html'


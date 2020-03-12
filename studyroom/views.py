from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import FormView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Quiz, Question, Answer, TakenQuiz
from .forms import QuestionForm, TakeQuizForm, TakenQuizForm

import json


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
        print("=== QuizDetail info === ")
        print(self.kwargs['slug'])
        slug = self.kwargs['slug']
        quiz = Quiz.objects.get(slug=slug)
        print(quiz)

        context = super().get_context_data(**kwargs)
        questions = Question.objects.filter(quiz=quiz).order_by('?')
        
        context['questions'] = questions
        context['now'] = timezone.now()
        
        return context

def getQuestionList(quiz, usr):
    # create question list 
    # based on quiz and user information 
    # qlist = [1, 2, 3, 4]

    qlist = []

    quiz = Quiz.objects.get(slug=quiz)
    questions = Question.objects.filter(quiz=quiz).order_by('?')[:3]

    
    for question in questions: 
        qlist.append(question.id)

    return qlist

def list2text(lst): 
    print ('list : ', lst)
    txt = json.dumps(lst)
    print ('txt :', txt)
    return txt

def text2list(txt):
    jsonDec = json.decoder.JSONDecoder()
    lst = jsonDec.decode(txt)
    return lst

def get_exam_questions(qlist):
    print("===== Log IN :: view get_exam_questions ===========")
    exams = Question.objects.all()

    ids = text2list(qlist)

    exams = Question.objects.filter(id__in=ids)
    return exams

def quizTest(request,slug):
    print("===== Log IN :: view quizTest ===========")
    #  who - user account 
    #  what - make a quiz ( if there is no quiz left.. )

    #  find all questions in the quiz.
    quiz = Quiz.objects.get(slug=slug)
    questions = Question.objects.filter(quiz=quiz)
    print('Number of questions: ', questions.count())

    #  find who user is... 
    user = request.user

    # save a quiz to be taken to a Model(TakenQuiz)
    # left_quiz = TakenQuiz.objects.filter(student=user, quiz=quiz, completed=False)[:1][0]
    left_quiz = TakenQuiz.objects.filter(student=user, quiz=quiz, completed=False).first()
    # print (left_quiz.count())
    if left_quiz is None: 
        print ('Create new quiz.... ')

        # create a quiz ( question-set )
        question_list = getQuestionList(slug, user)
        qlist_txt = list2text(question_list)
        print ('Selected questions : ', question_list)

        qinstance = TakenQuiz.objects.create(
                    student = user, 
                    quiz = quiz, 
                    questions = qlist_txt, 
                    curr_question = 0, 
                    answer = '[]', 
                    completed = False, 
                )
        

    else : 
        print ('We have uncompleted quiz.. ')
        qinstance = left_quiz
    

    print ('Question list : ', qinstance.questions)
    exams = get_exam_questions(qinstance.questions)

    # test : LIST to TEXT 
    # qlist_txt = list2text(question_list)
    # print (type(qlist_txt))
    # qlist_lst = text2list(qlist_txt)
    # print (type(qlist_lst))

    context = {'exams':exams
            ,'quiz':quiz
            ,'qinstance':qinstance
        } 

    return render(request, "studyroom/quizTest.html", context)


def quizTake(request, slug):
    print("===== Log IN :: view quizTake ===========")
    print(slug)
    quiz = Quiz.objects.filter(slug=slug)
    print(quiz)
    # questions = Question.objects.filter(text__startswith=slug)
    questions = Question.objects.filter(quiz=quiz[0])
    for question in questions: 
        print (question.pk,question.quiz, question.text)
        answers = Answer.objects.filter(question=question, correct=True)
        for ans in answers: 
            print (ans.pk, ans.content, ans.correct)
    
    
    # if request.user.is_authenticated:
    #     print (request.user)
    username = request.user
    print(username)

    quiz = quiz.first()
    question = questions.first()
    
    if request.method =='POST':
        form = TakeQuizForm(question=question, data=request.POST)
    else : 
        form = TakeQuizForm(question=question)

    context = { 
        'quiz': quiz, 
        'question': question, 
        'form': form
                }


    return render(request, 'studyroom/quizTake.html', context)

# class QuizTake(request, slug):

# class QuizTake(FormView):
#     print ("Log :: IN :: class QuizTake.. ")
#     form = QuestionForm
#     template_name = 'quizTake.html'
#     result_template_name = 'result.html'
#     single_complete_template_name = 'single_complete.html'


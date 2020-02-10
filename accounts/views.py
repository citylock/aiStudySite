from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User         # django 에서 정의한 User 모델 사용
from django.contrib import auth
from django.shortcuts import redirect

from .forms import SignupForm, SigninForm                       # 새로 생성한 폼을 추가 

# Create your views here.
def signup(request):
    #  To Do - 기존에 동일한 ID를 가진 유저가 있는 경우 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # form = SignupForm(request.POST)             # 신규 회원 가입
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else : 
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signupForm':form})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username = username, password = password)
        if user is not None: 
            auth.login(request, user)
            return redirect('home')
        else : 
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect!!', 'SigninForm':SigninForm()})
    return render(request, 'accounts/login.html', {'SigninForm':SigninForm()})

def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('home')


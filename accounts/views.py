from django.shortcuts import render
from django.contrib.auth.models import User         # django 에서 정의한 User 모델 사용
from django.contrib import auth
from django.shortcuts import redirect

from .forms import SignupForm, SigninForm                       # 새로 생성한 폼을 추가 

# Create your views here.
def signup(request):
    #  To Do - 기존에 동일한 ID를 가진 유저가 있는 경우 
    if request.method == "POST":
        form = SignupForm(request.POST)             # 신규 회원 가입
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']

                new_user.save()
                return redirect('home')
            else : 
                # password 가 서로 다른 경우 
                return render(request, 'accounts/signup.html', {'signupForm':SignupForm(), 'error':'패스워드가 서로 다름..'})

        # if request.POST["password1"] == request.POST["password2"]: 
        #     user = User.objects.create_user (
        #         username = request.POST["username"], 
        #         password = request.POST["password1"]
        #     )
        #     auth.login(request, user)
        #     return redirect('home')
        return render(request, 'accounts/signup.html')
    elif request.method == "GET":                   # 사용자 데이터 입력전 
        return render( request, 'accounts/signup.html', {'signupForm':SignupForm()}) 

    return render(request, 'accounts/signup.html',{'signupForm':SignupForm()})

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
    return redirect('home')


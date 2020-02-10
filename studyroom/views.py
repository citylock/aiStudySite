from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'studyroom/home.html', {'count': count})
    


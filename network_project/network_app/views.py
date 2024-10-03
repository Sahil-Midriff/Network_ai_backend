from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Welcome to home')

def signup(request):
    return render(request,'./templates/signup.html')


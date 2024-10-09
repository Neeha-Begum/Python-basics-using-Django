from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def func1(request):
    return render(request,'extend.html')
def func2(request):
    return render(request,'about.html')
def func3(request):
    return render(request,'contact.html')
def func4(request):
    return render(request,'help.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request,sname):
    res=(sname==sname[::-1])
    d={'result':res}
    return render(request,'palindrome.html',d)
def func2(request,num):
    res=(num>0)
    d={'result':res}
    return render(request,'postive.html',d)
def func3(request,num):
    res=(num%2==0)
    d={'result':res}
    return render(request,'even.html',d)
def func4(request,num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    res=(count==2)
    d={'result':res}
    return render(request,'prime.html',d)
from django.shortcuts import render
from django.http import HttpResponse

d={'results':[{'rollno':1,'name':'Alice','cgpa':8,'subjects':57,'failed_subjects':0},
            {'rollno':2,'name':'Jhon','cgpa':7,'subjects':56,'failed_subjects':1},
            {'rollno':3,'name':'kate','cgpa':8,'subjects':57,'failed_subjects':0},
            {'rollno':4,'name':'Tom','cgpa':6,'subjects':52,'failed_subjects':5},
            {'rollno':5,'name':'Sam','cgpa':7,'subjects':55,'failed_subjects':2}]}

# Create your views here.
def Func(request,rollno):
    result=None
    for record in d.get('results'):
        if record.get('rollno')==rollno:
            result=record
            break
    if result is not None:
        return render(request,'results.html',{'r':result})
    else:
        return render(request,'results.html')
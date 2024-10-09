from django.urls import path
from app3 import views

urlpatterns=[
    path('exam/<int:rollno>',views.Func,name="e1"),
]
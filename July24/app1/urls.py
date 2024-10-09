from django.urls import path
from app1 import views

urlpatterns=[
    path('palindrome/<str:sname>',views.func1,name="p1"),
    path('pos/<int:num>',views.func2,name='p1'),
    path('even/<int:num>',views.func3,name='e1'),
    path('prime/<int:num>',views.func4,name='p2')
]
from django.urls import path
from app2 import views

urlpatterns=[
    path('home',views.func1,name="h1"),
    path('about',views.func2,name="a1"),
    path('contact',views.func3,name="c1"),
    path('help',views.func4,name="h1")
]
from multiprocessing.connection import answer_challenge
from pathlib import Path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question', views.postQuestion, name='postQuestion'),
    path('answer', views.postAnswer, name='postAnswer'),
    path('delete', views.deleteQuestion, name='deleteQuestion'),
    path('vote', views.answerVote, name='answerVote'),
    path('signup', views.signup, name='signup')
]

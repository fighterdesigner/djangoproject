import imp
from multiprocessing.connection import answer_challenge
from random import choice
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template import context
from .models import Question, Choice
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pub_date')[:3]
    context = {'questions': questions}
    return render(request, 'index.html', context)

def postQuestion(request):
    if request.method == 'POST':
        question = Question()
        question.question_text = request.POST.get('question_text')
        question.pub_date = timezone.now()
        question.user = request.user
        question.save()
        return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/') 

def postAnswer(request):
    if request.method == 'POST':
        question = Question.objects.get(pk=request.POST.get('question_id'))
        answer = Choice()
        answer.choice_text = request.POST.get('choice_text')
        answer.user = request.user
        answer.questions = question
        answer.save()
        return HttpResponseRedirect('/') 

def deleteQuestion(resquest):
        Question.objects.get(pk=resquest.POST.get('question_id')).delete()
        return HttpResponseRedirect('/')

def answerVote(resquest):
    answer = Choice.objects.get(pk=resquest.POST.get('id'))

    if resquest.POST.get('vote_up'):
        answer.votes += int(resquest.POST.get('vote_up'))
        answer.save()
    if resquest.POST.get('vote_down'):
        answer.votes -= int(resquest.POST.get('vote_down'))
        answer.save()

    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)
           

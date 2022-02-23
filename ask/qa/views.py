from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from qa.forms import AskForm , AnswerForm
from qa.models import Answer, Question
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse, resolve
from django.shortcuts import render, redirect
 

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

def testCookie(response):
    response.set_cookie('myCookie',"12345")
    return response



def questions_list(request):
    question = Question.objects.new()
    page = request.GET.get('page',1)
    paginator = Paginator(question, 10)
    paginator.baseurl = reverse("index") + "?page="
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(1)
    content = {
        "user": request.user,
        "question": question,
        "paginator": paginator,
        "page": page,
        }
    return testCookie(render(request, "question_list.html", content))


def details_question(request, id):
    question = get_object_or_404(Question,id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.question = question
            comment.save()
            form = AnswerForm()
        # return redirect('details', id=post.id)
    else:
        form = AnswerForm(initial={'question': question.id})

    answer = Answer.objects.filter(question=question)
    content = {
        "user": request.user,
        "question": question,
        "answer": answer,
        "form": form,
        }
    return render(request, "question_one.html", content)

def popular(request):
    question = Question.objects.popular()
    page = request.GET.get('page',1)
    paginator = Paginator(question, 10)
    paginator.baseurl = reverse("popular") + "?page="
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(1)
    print(page)
    content = {
        "user": request.user,
        "question": question,
        "paginator": paginator,
        "page": page,
        }
    return render(request, "question_list.html", content)
 
def ask_new(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('details', id=post.id)
    else:  
        form = AskForm()
    return render(request, 'new_question.html', {'form': form})  


def signup(request):

    return

def login_view(request): 
    
    if request.method == "POST":
        form_auth = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user, form_auth.is_valid())
        if form_auth.is_valid() :
            login(request, user)
            print(user)
            return redirect('index')
    else:
        form_auth = AuthenticationForm()

    return render(request, 'login.html' , {"form_auth":form_auth})  

    
def logout_view(request):
    logout(request)
    return redirect('index')
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from qa.forms import AskForm , AnswerForm
from qa.models import Answer, Question
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse, resolve
from django.shortcuts import render, redirect
 


def questions_list(request):
    question = Question.objects.new()
    page = request.GET.get('page',1)
    paginator = Paginator(question, 10)
    paginator.baseurl = reverse("index") + "?page="
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(1)
    print(page)
    content = {
        "question": question,
        "paginator": paginator,
        "page": page,
        }
    return render(request, "question_list.html", content)
    # try:
    #     answers = quest.objects.filter()

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
        form = AnswerForm()

    answer = Answer.objects.filter(question=question)
    content = {
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
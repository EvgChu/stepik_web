from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from qa.models import Answer, Question
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse, resolve
from django.shortcuts import render

def test(request, *args, **kwargs):
    return HttpResponse('OK')


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
    answer = Answer.objects.filter(question=question)
    content = {
        "question": question,
        "answer": answer
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
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from qa.models import Question
from django.core.paginator import Paginator
from django.urls import reverse, resolve
from django.shortcuts import render

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def questions_list(request):
    question = Question.objects.new()
    limit = request.GET.get('limit',3)
    page = request.GET.get('page',1)
    paginator = Paginator(question, limit)
    paginator.baseurl = reverse("index") + "?page="
    paginator.question_url = "question/"
    page = paginator.page(page)
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

    return HttpResponse('OK' + str(id))

def popular(request):

    return HttpResponse('OK')
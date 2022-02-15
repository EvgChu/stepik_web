from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from qa.models import Question
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import render

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def questions_list(request):
    question = Question.objects.new()
    limit = request.GET.get('limit',2)
    page = request.GET.get('page',1)
    paginator = Paginator(question, limit)
    paginator.baseurl = "?page="
    page = paginator.page(page)
 
    return render(request, "question_list.html", {
        "question": question,
        "paginator": paginator,
        "page": page,
        }
    )
    # try:
    #     answers = quest.objects.filter()

def one_question(request, id):

    return HttpResponse('OK' + str(id))

def popular(request):

    return HttpResponse('OK')
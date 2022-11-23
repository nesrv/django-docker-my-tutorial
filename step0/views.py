from django.http import HttpResponse
from django.views.generic import FormView

from .models import *


# Create your views here.


def index(request):
    # print (dir(request))
    return HttpResponse("index")


def test(request):
    return HttpResponse("<h1>test</h1>")


# class TestFormView(FormView):
#     model = News
#     template_name = "step0/index.html"


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

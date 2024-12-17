from django.shortcuts import render
from django.http import HttpResponse
import random


def text_response(request):
    return HttpResponse(f"это текстовый ответ из API {random.randint (1, 100)}")


def html_view(request):
    return render(request, "base.html")
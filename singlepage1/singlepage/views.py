from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = [
    "Hello World!",
    "My name is Danil",
    "My girlfriend is Varya"
]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    return Http404("No such section")
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request):

    # Get start and end points
    start = int(request.GET["start"] or 0)
    end = int(request.GET["end"] or (start + 9))

    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    return JsonResponse({
        "posts": data
    })
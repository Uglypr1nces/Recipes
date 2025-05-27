from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, worldfssd. You're at the polls index.")
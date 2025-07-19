from django.http import HttpResponse

def index(request):
    return HttpResponse("hello biswaa welcome. Lets do it")

def about(request):
    return HttpResponse("you are allsett.")
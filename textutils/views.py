from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'biswa', 'place':'Mars'}
    return render(request, 'index.html',params)

def about(request):
    return HttpResponse("you are allsett.")

def removepunc(request):
    return HttpResponse("remove punc")

def newlineremove(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("captalize first")

def charcount(request):
    return HttpResponse("charcount")

def spaceremove(request):
    return HttpResponse("spaceremove <a href = '/'>back</a>")
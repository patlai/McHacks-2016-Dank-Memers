from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("jet fuel can't melt dank memes")

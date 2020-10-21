from django.shortcuts import render

from django.http import HttpResponse

def hellow(request):
    return HttpResponse('wellcome django first class')
# Create your views here.

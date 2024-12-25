from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def january(request):
    return HttpResponse('Don\'t drink alcohol for the month.')

def february(request):
    return HttpResponse('Don\'t eat meat for the month.')
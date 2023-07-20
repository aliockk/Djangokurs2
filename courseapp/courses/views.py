from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import redirect ,render

def  site(request):
    return  HttpResponse('site içerigi gizlidir.')

def GetInfo(request,Info):
    return HttpResponse(Info)

def getKnowledge(request,category):
    return HttpResponse(f"{category} budur.")
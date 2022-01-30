from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicial(request):
    return render(request,"home.html", {"password":"abcdefghijk"})


def password(request):
    return HttpResponse("1+1 =" )
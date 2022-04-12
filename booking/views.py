from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_home(request):
    # return HttpResponse('Hello World')
    return render(request,'home.html')

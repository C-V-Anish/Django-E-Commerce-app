from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Create your views here.
def index(request):
    return render(request,'index1.html')

def blogpost(request):
    return render(request,"blogpost.html")

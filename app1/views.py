from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'input.html')
def add(request):
    X=request.GET["t1"]
    Y=request.GET["t2"]
    i=int(X)
    j=int(Y)
    z=i+j
    res=HttpResponse("the sum is:"+str(z))
    return res
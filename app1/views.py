from django.shortcuts import render

# Create your views here.
def max(request):
    return render(request,'max.html')
def min(request):
    return render(request,'min.html')

from django.shortcuts import render

# Create your views here.
def find(request):
    return render(request,'find.html')
def temp(request):
    return render(request,'temp.html')


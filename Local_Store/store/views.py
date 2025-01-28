# for rendering the html file

from django.shortcuts import render

def home(request):
    return render(request, 'store/home.html')
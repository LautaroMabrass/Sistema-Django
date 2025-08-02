from django.http import HttpResponse
from django.shortcuts import render

# Index vista
def index(request):
    return render(request, 'index.html')

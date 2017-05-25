from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def createUser(request):
  if request.method != 'POST':
    return redirect('/')
  else:
    # User.objects.validateUser(request.POST)
    return redirect('/')

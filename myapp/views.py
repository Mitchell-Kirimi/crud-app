from django.shortcuts import render
from .models import User

# Create your views here.
def index (request):
    post=User.objects.all()
    return render(request,'index.html')

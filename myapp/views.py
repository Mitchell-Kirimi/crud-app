from django.shortcuts import render, redirect
from yt_dlp.utils import args_to_str

from .models import User
from .forms import UserForm
# Create your views here.
def User_list(request):
    users=User.objects.all()
    return render(request,'listingpage.html',{'users':users})

def adduser(request):
    mydict={}
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form']= form
    return render(request, 'add.html', mydict)


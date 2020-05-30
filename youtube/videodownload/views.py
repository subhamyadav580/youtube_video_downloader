from django.shortcuts import render
from pytube import YouTube
import os.path
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        homedir = os.path.expanduser("~")
        dirs = homedir + '/Downloads'
        url = request.POST['link']
        YouTube(url).streams.first().download(homedir + '/Downloads')
        messages.success(request, 'video downloaded!.Check your Download directory')
        return render(request, 'home.html')
    return render(request, 'home.html')

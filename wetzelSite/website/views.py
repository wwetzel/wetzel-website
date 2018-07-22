from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main.html')

def test(request):
    return render(request, 'portfolio.html')

def killingPopMusic(request):
    return render(request, 'killing-pop-music.html')

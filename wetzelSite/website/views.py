from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def main(request):
    import random
    randomNumber = random.random()
    randomNumber = str(randomNumber)
    randomNumber = randomNumber[1:]
    return render(request, 'main.html', {'randomNumber':randomNumber})

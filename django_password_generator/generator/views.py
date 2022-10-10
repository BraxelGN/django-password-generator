from django.shortcuts import render
import random


def about(request):
    return render(request,'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    character = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''

    lenght = int(request.GET.get('lenght'))
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        character.extend(list("!@$%&/()=?¿,.-"))
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))
    for x in range (lenght):
        generated_password += random.choice(character)
    return render(request, 'password.html', {'password': generated_password})


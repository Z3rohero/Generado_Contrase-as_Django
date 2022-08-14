from django.shortcuts import render
import random
import string

#from django.http import HttpResponse


#informacion de cliente
def about(request):
    return render(request, 'about.html')


#home
def home(request):
    return render(request, 'home.html')


def password(request):
    caract = list(string.ascii_lowercase)
    longitud = int(request.GET.get('longitud'))
    ge_password = " "
    if request.GET.get('mayuscula'):
        caract.extend(list(string.ascii_uppercase))
    if request.GET.get('especial'):
        caract.extend(list("!@#$&"))
    if request.GET.get('numeros'):
      caract.extend(list("0123456789"))
    for x in range(longitud):
        ge_password += random.choice(caract)
    return render(request, 'password.html', {'passw': ge_password})

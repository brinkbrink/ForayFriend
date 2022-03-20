from django.shortcuts import render
from .models import Foraged, ForageType, Season, Foray, Resource

# Create your views here.
def index(request):
    return render(request, 'friend/index.html')

def foraged(request):
    foraged_list=Foraged.objects.all()
    return render(request, 'friend/foraged.html', {'foraged_list': foraged_list})
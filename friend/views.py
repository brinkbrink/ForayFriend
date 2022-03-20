from django.shortcuts import get_object_or_404, render
from .models import Foraged, ForageType, Season, Foray, Resource
from .forms import ForagedForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'friend/index.html')

def foraged(request):
    foraged_list=Foraged.objects.all()
    return render(request, 'friend/foraged.html', {'foraged_list': foraged_list})

def forageDetail(request, id):
    foraged=get_object_or_404(Foraged, pk=id)
    return render(request, 'friend/foragedetail.html', {'foraged' : foraged})

@login_required
def newForaged(request):
    form=ForagedForm

    if request.method=='POST':
        form=ForagedForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ForagedForm()
    else: 
        form=ForagedForm()
    return render(request, 'friend/newforaged.html', {'form':form})

def loginmessage(request):
    return render(request, 'friend/loginmessage.html')

def logoutmessage(request):
    return render(request, 'friend/logoutmessage.html')
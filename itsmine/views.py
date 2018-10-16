from django.shortcuts import render,redirect
from .models import Member_Details
from .forms import RegForm,LoginForm,UserCreationForm
from django.http import HttpResponseRedirect
from django import forms
# Create your views here.

def home(request):
    return render(request,'home.html')

def reg(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            ema=form.cleaned_data['email']
            pwd=form.cleaned_data['password']
            if not (Member_Details.objects.filter(username=un).exists() or Member_Details.objects.filter(email=ema).exists()):
                form.save()
                return HttpResponseRedirect('itsmine:home')
            data=Member_Details.objects.get(username=form.cleaned_data['username'])
            return render(request,'display.html',{'reg':data})
    else:
        form=RegForm()
    return render(request,'reg.html',{'reg':form})
def logi(request):
    if request.method=='POST':
        logi=LoginForm(request.POST)
        if logi.is_valid():
            suc=Member_Details.objects.filter(username=logi.cleaned_data['username'],password=logi.cleaned_data['password'])
            if not suc:
                return redirect('itsmine:reg')
            else:
                raise forms.ValidationError()
        else:
            return redirect('itsmine:login')
    else:
        logi=LoginForm()
        return render(request,'logi.html',{'logi':logi})

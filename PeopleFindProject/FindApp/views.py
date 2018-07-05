from django.shortcuts import render,redirect,reverse
from .models import Profiles,Department,Position,ProfilesForm,PositionForm,JobDiscriptionForm,SubDivisionForm,DivisionForm,JobDiscription
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
# from django.contrib.auth import user
from django.contrib.auth.models import User
# Create your views here.

# @login_required
def Profile(request):
    department  = Department.objects.all().values('name')
    profile     = Profiles.objects.all()
    context     = {'profile' : profile , 'department':department} 
    return render(request,'profile2.html',context)
    

def page(request,pk):
    profile     = Profiles.objects.all().filter(pk=pk).values('pk', 'prefix_name','name','mid_name','last_name','image','email','table_no','position','room_no','department','memo','phone')[0]
    print(profile)
    position    = Position.objects.all().filter(pk=profile['position']).values('title')[0]
    department  = Department.objects.all().filter(id=profile['department']).values('name')[0]
    context     = {'profile' : profile ,'position' : position ,'department' : department}
    return render(request,'page.html',context)

@login_required
def form(request):
    user = request.user
    print(type(user),user)
    if request.method == 'POST':
        profile = Profiles.objects.all().filter(account=user)[0]
        form    = ProfilesForm(request.POST, request.FILES, instance=profile)
        if form.is_valid() :
            form.save()
            return redirect(reverse('FindApp:form2'))
    else:
        profile = Profiles.objects.all().filter(account=user)[0]
        form    = ProfilesForm(instance=profile)
        context = {'form':form}
    return render(request,'form2.html',context)

def form2(request):
    user = request.user
    print(type(user),user)
    profile     = Profiles.objects.all().filter(account=user)[0]
    discription = JobDiscription.objects.filter(position=profile.position)
    if request.method=='POST':
        formJobdiscription  = JobDiscriptionForm(request.POST)
        if formJobdiscription.is_valid() :
            formJobdiscription.save()
        return redirect(reverse('FindApp:profile'))
    else:
        profile     = Profiles.objects.all().filter(account=user)[0]
        discription = JobDiscription.objects.filter(position=profile.position)
        formJobdiscription  = JobDiscriptionForm(instance=profile)
        context     = {'formJobdiscription':formJobdiscription}
    return render(request,'form3.html',context)
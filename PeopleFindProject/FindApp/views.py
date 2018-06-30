from django.shortcuts import render,redirect,reverse
from .models import Profiles,Department,Position,ProfilesForm,PositionForm,JobDiscriptionForm,SubDivisionForm,DivisionForm
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
    # return render(request,'profile.html',context)
    return render(request,'profile2.html',context)
    

def page(request,pk):
    profile     = Profiles.objects.all().filter(pk=pk).values('pk', 'prefix_name','name','mid_name','last_name','image','email','table_no','position','room_no','department','memo')[0]
    position    = Position.objects.all().filter(profile=profile['position']).values('title')[0]
    department  = Department.objects.all().filter(id=profile['department']).values('name')[0]
    context     = {'profile' : profile ,'position' : position ,'department' : department}
    return render(request,'page.html',context)

# @login_required
# def form(request,pk):
#     profile    = Profiles.objects.all().filter(pk=pk)[0]
#     if request.method == 'POST':
#         form = ProfilesForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             # print(form)
#             form.save()
#             return redirect(reverse('FindApp:profile'))
#             # return redirect('/')
#     else:
#         print(profile)
#         form = ProfilesForm(instance=profile)
#     return render(request,'form2.html',{'form':form})

@login_required
def form(request):
    user = request.user.id
    print(type(user),user)
    if request.method == 'POST':
        profile    = Profiles.objects.all().filter(pk=user)[0]
        form = ProfilesForm(request.POST, request.FILES, instance=profile)
        formPosition = PositionForm(request.POST)
        if form.is_valid() and formPosition.is_valid:
            # print(form)
            form.save()
            formPosition.save()
            return redirect(reverse('FindApp:profile'))
    else:
        profile = Profiles.objects.all().filter(pk=user)[0]
        position = Position.objects.all().filter(pk=user)[0]
        print(position)
        print(profile)
        form = ProfilesForm(instance=profile)
        formPosition = PositionForm()
        # formPosition = PositionForm(isinstance=position)
        formJobdiscription = JobDiscriptionForm()
        formSubdivision = SubDivisionForm()
        formDivision = DivisionForm()
        context = {'form':form,'formPosition':formPosition,'formJobdiscription':formJobdiscription,'formSubdivision':formSubdivision,'formDivision':formDivision}
    return render(request,'form2.html',context)

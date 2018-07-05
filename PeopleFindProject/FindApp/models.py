import json
import requests
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.core.validators import RegexValidator
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name

class Division(models.Model):
    title        = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.title

class SubDivision(models.Model):
    title       = models.CharField(max_length=50,null=True,blank=True)
    division    = models.ForeignKey(Division,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.title

class Position(models.Model):
    title       = models.CharField(max_length=50,null=True,blank=True)
    subdivision = models.ForeignKey(SubDivision,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        # return self.title
        return '%s %s'%(self.title,self.subdivision)

# class Profiles(models.Model):
#     account     = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
#     role        = models.IntegerField()
#     prefix_name = models.CharField(max_length=50,null=True)
#     name        = models.CharField(max_length=50,null=True)
#     mid_name    = models.CharField(max_length=50,null=True,blank=True)
#     last_name   = models.CharField(max_length=50,null=True)
#     image       = models.ImageField(upload_to='image/',null=True,blank=True)
#     email       = models.EmailField(max_length=100,null=True)
#     table_no    = models.CharField(max_length=50,null=True,blank=True)
#     room_no     = models.CharField(max_length=50,null=True,blank=True)
#     position    = models.ForeignKey(Position,on_delete=models.SET_NULL,null=True)
#     department  = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
#     phone       = PhoneNumberField()
#     memo        = models.CharField(max_length=99,null=True,blank=True)
#     def __str__(self):
#         return self.name

class Profiles(models.Model):
    account     = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    role        = models.IntegerField()
    prefix_name = models.CharField(max_length=50,null=True)
    name        = models.CharField(max_length=50,null=True)
    mid_name    = models.CharField(max_length=50,null=True,blank=True)
    last_name   = models.CharField(max_length=50,null=True)
    image       = models.ImageField(upload_to='image/',null=True,blank=True)
    email       = models.EmailField(max_length=100,null=True)
    table_no    = models.CharField(max_length=50,null=True,blank=True)
    room_no     = models.CharField(max_length=50,null=True,blank=True)
    position    = models.ForeignKey(Position,on_delete=models.SET_NULL,null=True)
    department  = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Phone number must be entered in the format: '0x00000000 or 0200000000'. ")
    phone       = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    memo        = models.CharField(max_length=99,null=True,blank=True)
    def __str__(self):
        return self.name

class JobDiscription(models.Model):
    discription   = models.CharField(max_length=99,null=True,blank=True)
    position      = models.ForeignKey(Position,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.discription

class ProfilesForm(ModelForm):
    class Meta:
        model   = Profiles
        fields  = '__all__'
        labels  = {
            "prefix_name" : _("คำนำหน้า")
        }
        exclude = ['account','role']
class PositionForm(ModelForm):
    class Meta:
        model   = Position
        fields  = '__all__'
class JobDiscriptionForm(ModelForm):
    class Meta:
        model   = JobDiscription
        fields  = '__all__'
        # exclude = ['position']
class SubDivisionForm(ModelForm):
    class Meta:
        model   = SubDivision
        fields  = '__all__'
        # exclude = ['position']
class DivisionForm(ModelForm):
    class Meta:
        model   = Division
        fields  = '__all__'

def logged_in_handle(sender, user, request, **kwargs):
    ROLE = {
        'STUDENT': '1',

    }
    #
    # Check if TU login
    prov = user.social_auth.filter(provider='tu')
    if prov.exists():
        data    = prov[0].extra_data
        headers = {
            "Authorization": "Bearer {}".format(data['access_token'])
        }
        api  = requests.get('https://api.tu.ac.th/api/me/', headers=headers).json()
        if api['company'] == 'คณะวิทยาศาสตร์และเทคโนโลยี':
            if api['role'] == ROLE['STUDENT']:
                print("API : ", api)
                print("api['username'] :", api['username'])
                print(Profiles.objects.all())
                index   = User.objects.all().filter(username = api['username'])[0]
                profile = Profiles.objects.filter(account = index)
                print("Profile : ", profile)
                if not profile.exists():
                    print("profile not exists")
                    create_init_department = Department.objects.update_or_create(
                        name=api['department'])
                    create_init_profile     = Profiles.objects.create(
                        account = index,
                        name    = api['firstname'],
                        role    = api['role'],
                        last_name = api['lastname'],
                    )
user_logged_in.connect(logged_in_handle)


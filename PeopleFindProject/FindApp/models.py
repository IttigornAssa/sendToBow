from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name

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
    department  = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    phone       = PhoneNumberField()
    memo        = models.CharField(max_length=99,null=True,blank=True)
    def __str__(self):
        return self.name

class Position(models.Model):
    title    = models.CharField(max_length=50,null=True,blank=True)
    profile  = models.ForeignKey(Profiles,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return "%s %s" % (self.title,self.profile)
class JobDiscription(models.Model):
    discription        = models.CharField(max_length=59,null=True,blank=True)
    position           = models.ForeignKey(Position,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name
class SubDivision(models.Model):
    name        = models.CharField(max_length=50,null=True,blank=True)
    position    = models.ForeignKey(Position,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name
class Division(models.Model):
    name        = models.CharField(max_length=50,null=True,blank=True)
    subdivition = models.ForeignKey(SubDivision,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class ProfilesForm(ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'
        labels = {
            "prefix_name" : _("คำนำหน้า")
        }

        # exclude = ['prefix_name']
        # fields = ('prefix_name','name','mid_name','last_name','image','email','table_no','position','room_no','department','memo')
        # exclude = ('prefix_name','name','mid_name','last_name','image','email','table_no','position','room_no','department','memo')
from django.contrib import admin
from .models import Profiles,Department,Division,SubDivision,JobDiscription,Position
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Department._meta.fields]
class ProfileAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Profiles._meta.fields]
class PositionAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Position._meta.fields]
class JobDiscriptionAdmin(admin.ModelAdmin):
    list_display=[f.name for f in JobDiscription._meta.fields]
class DivisionAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Division._meta.fields]
class SubDivisionAdmin(admin.ModelAdmin):
    list_display=[f.name for f in SubDivision._meta.fields]
admin.site.register(Profiles,ProfileAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Division,DivisionAdmin)
admin.site.register(SubDivision,SubDivisionAdmin)
admin.site.register(JobDiscription,JobDiscriptionAdmin)
admin.site.register(Position,PositionAdmin)
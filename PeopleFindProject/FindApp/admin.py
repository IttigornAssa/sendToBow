from django.contrib import admin
from .models import Profiles,Department,Division,SubDivision,JobDiscription,Position
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Department._meta.fields]
class ProfileAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Profiles._meta.fields]
class PositionAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Position._meta.fields]
admin.site.register(Profiles,ProfileAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Division)
admin.site.register(SubDivision)
admin.site.register(JobDiscription)
admin.site.register(Position,PositionAdmin)
from django.contrib import admin
from .models import Nurse,Patsient, PersonalInfo, Doctor,SeniorDoctor,Admin
# Register your models here.
admin.site.register(PersonalInfo)

@admin.register(Nurse)
class Nurse(admin.ModelAdmin):
    list_display = ['name','email', 'patsient','mobile','images','city']
    # list_filter = ['in_stock', 'is_active']



@admin.register(Patsient)
class Patsient(admin.ModelAdmin):
    list_display = ['personal_info',]
    # list_filter = ['in_stock', 'is_active']


@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = ['personal_info','nurse','patsient']
    # list_filter = ['in_stock', 'is_active']


@admin.register(SeniorDoctor)
class SeniorDoctor(admin.ModelAdmin):
    list_display = ['personal_info','doctor','nurse','patsient']


@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = ['nurse','senior_doctor','doctor','nurse',]



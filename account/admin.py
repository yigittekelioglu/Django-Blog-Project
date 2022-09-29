from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from account.models import Profile
from django.contrib.auth.admin import UserAdmin
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'gender', 'birthdate', 'is_active', 'is_staff')
    list_filter = ('gender', 'is_active', 'is_staff')

admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)#grupu gorunmez yaparx


# Register your models here.

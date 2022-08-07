from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from usersapp.models import UsersTodo

admin.site.register(UsersTodo, UserAdmin)




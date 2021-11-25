from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list = ('name', 'phone', 'api_id', 'api_hash')


admin.site.register(User, UserAdmin)

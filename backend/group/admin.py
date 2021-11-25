from django.contrib import admin
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list = ('group_name', 'group_id')


admin.site.register(Group, GroupAdmin)

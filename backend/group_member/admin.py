from django.contrib import admin
from .models import GroupMember


class GroupMemberAdmin(admin.ModelAdmin):
    list = ('name', 'phone', 'api_id', 'api_hash')


admin.site.register(GroupMember, GroupMemberAdmin)

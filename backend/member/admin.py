from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list = ('member_id', 'member_name', 'access_hash')


admin.site.register(Member, MemberAdmin)

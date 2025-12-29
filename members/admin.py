from django.contrib import admin

from members.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_type', 'designation', 'department', 'email', 'phone')
    search_fields = ('name', 'designation', 'department', 'email')
    list_filter = ('member_type', 'department')

admin.site.register(Member, MemberAdmin)
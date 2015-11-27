from django.contrib import admin

from models import User, Group, Message

class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'info')

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'age', 'active')


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Message)


# Register your models here.

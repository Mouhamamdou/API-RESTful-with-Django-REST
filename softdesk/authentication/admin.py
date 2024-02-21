from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'can_data_be_shared', 'can_be_contacted', 'age')


admin.site.register(User, UserAdmin)

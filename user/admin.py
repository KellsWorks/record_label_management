from django.contrib import admin

from user.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')
    search_fields = (["username"])
    list_filter = ('username', 'email', 'first_name', 'last_name', 'role')
    list_per_page = 10

admin.site.register(User, UserAdmin)

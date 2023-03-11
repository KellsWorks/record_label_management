from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User, Profile


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = (["username"])
    list_filter = ('username', 'email', 'first_name', 'last_name')
    list_per_page = 10


admin.site.register(User, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (['user'])

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Profile, UserProfileAdmin)

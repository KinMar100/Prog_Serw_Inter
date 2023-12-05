from django.contrib import admin

from . models import User

# Register your user model here.
# in admin panel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['id', 'email', 'name', 'date_added', 'last_login']
    list_filter = ['id']
    ordering = ['id']

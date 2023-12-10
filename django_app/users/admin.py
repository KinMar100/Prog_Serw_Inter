from django.contrib import admin

from . models import User, Rank

# Register your user model here.
# in admin panel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['id', 'email', 'name', 'date_added', 'last_login', 'rank']
    list_filter = ['id']
    ordering = ['id']


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['id']
    ordering = ['id']

# done

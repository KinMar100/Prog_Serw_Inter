from django.contrib import admin
from .models import Post, Comment, Reaction

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'description', 'add_date', 'edit_date', 'user']
    list_filter = ['title']
    ordering = ['id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['user', 'post']
    list_display = ['id', 'description', 'post', 'user', 'add_date', 'edit_date']
    list_filter = ['id']
    ordering = ['id']


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    search_fields = ['post', 'user']
    list_display = ['id', 'post', 'type_of_reaction', 'user', 'add_date']
    list_filter = ['id']
    ordering = ['id']

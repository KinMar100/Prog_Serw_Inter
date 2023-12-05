from django.contrib import admin
from .models import Question, Choice, Category
# Register your poll models here.
# in admin panel


class ChoicesInLine(admin.StackedInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'question_text', 'category', 'pub_date']
    list_filter = ['name']
    inlines = [ChoicesInLine]
    ordering = ['id']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text', 'question', 'votes']
    list_filter = ['choice_text']
    ordering = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# done

from django.contrib import admin
from .models import Question, Choice, Category


# Register your models here.
# admin panel

class ChoicesInLine(admin.StackedInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'question_text', 'category']
    list_filter = ['name']
    inlines = [ChoicesInLine]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text', 'question', 'votes']
    list_filter = ['choice_text']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# done

from django.contrib import admin

from .models import Choice, Question


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["publish_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["publish_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInLine]
    list_display = ["question_text", "publish_date", "was_published_recently"]
    list_filter = ["publish_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)

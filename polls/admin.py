from django.contrib import admin
from .models import Question, Choice


# ADMIN FOR CHOICES
# admin.site.register(Choice) # This makes choices appear but as if it were unrelated to a question. Not efficent

# class ChoiceInLine(admin.StackedInline): # StackedInLine = Shows this field line by line - Visually large!
#     model = Choice
#     extra = 1


class ChoiceInLine(admin.TabularInline):  # TabularLine = Shows this field as a table - Visually Small!
    model = Choice
    extra = 0


# ADMIN FOR QUESTIONS
class QuestionAdmin(admin.ModelAdmin):
    # Indicate django to show these fields right away when acesse Question list
    list_display = ('question_text', 'get_id', 'pub_date', 'future_question', 'was_published_recently',
                    'get_total_votes',)

    list_filter = ['pub_date']

    search_fields = ['question_text']

    # More complete form to diplay for each questions
    fieldsets = [
        (None, {'fields': ('question_text',)}),
        ('Date Information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInLine]  # inlines = Indicates to django what to display along with each question.

    # Simple way to chose and order display in admin
    # fields = [
    #     'pub_date',
    #     'question_text',
    # ]


# NEVER FORGET TO REGISTER() TO BE DISPLAYED ONLINE
admin.site.register(Question, QuestionAdmin)

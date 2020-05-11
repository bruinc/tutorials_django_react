from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline): # StackedInline for vertical list
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # Display fields on the questions page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Adds a filter sidebar that lets people filter the change list by pub_date
    list_filter = ['pub_date']
    # Adds a search box at top of change list
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

""" class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin) """

""" class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text'] """

# Tell admin that Question objects have an admin interface
#admin.site.register(Question)

# Just this line creates an "add choice" form that includes a dropdown to pick the 
# corresponding question.
# admin.site.register(Choice)




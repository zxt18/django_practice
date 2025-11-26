from django.contrib import admin
from .models import Question, Choice
# Register your models here.





# admin.site.register(Question)
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra =  3

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date","question_text"]
    list_display = ["question_text", "pub_date", "was_published_recently"] #This changes the list display
    inlines = [ChoiceInLine] 

admin.site.register(Question,QuestionAdmin)

# admin.site.register(Choice)
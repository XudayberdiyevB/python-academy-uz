from django.contrib import admin
from .models import Exam, Question, Answer

class AnswerAdmin(admin.ModelAdmin):
    list_filter = ('question',)

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('exam',)

# Register your models here.
admin.site.register(Exam)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
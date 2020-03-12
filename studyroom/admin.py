from django.contrib import admin
from .models import Quiz, Question, TakenQuiz, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4
    max_num = 5

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',) 
    # filter_horizontal = ('quiz',)   # many-to-many field
    inlines = [AnswerInline]

# Register your models here.
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(TakenQuiz)
# admin.site.register(Answer)



from django.contrib import admin
from .models import QuizModel, QuizAdd


class QuizModelAdmin(admin.ModelAdmin):
    list_display = ('quiz_name', 'answer_key', 'quiz_file', 'publishing_date')

    class Meta:
        model = QuizModel


class QuizAddAdmin(admin.ModelAdmin):
    list_display = ('department', 'number', 'name', 'quiz_name', 'answer_key', 'answer', 'quiz_result', 'publishing_date')

    class Meta:
        model = QuizAdd


admin.site.register(QuizModel, QuizModelAdmin)
admin.site.register(QuizAdd, QuizAddAdmin)

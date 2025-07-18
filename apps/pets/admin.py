from django.contrib import admin
from .models import Pet, Exam, ExamResult

admin.site.register(Pet)
admin.site.register(Exam)
admin.site.register(ExamResult)

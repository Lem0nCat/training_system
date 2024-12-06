from django.contrib import admin
from .models import Test, Result, Question, TestResult


admin.site.register(Test)
admin.site.register(Result)
admin.site.register(Question)
admin.site.register(TestResult)

from django.db import models
from django.contrib.auth.models import AbstractUser

from tests.models import Question, Result, TestResult



class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    teacher = models.BooleanField(default=0)
    results = models.ManyToManyField(Question,  through=Result)
    
    def is_teacher(self):
        return bool(self.teacher)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



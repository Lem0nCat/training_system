from django.db import models


class Test(models.Model):
    possible_points = models.IntegerField()
    lecture = models.OneToOneField('lectures.Lecture', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'Тест №{self.lecture.id} - {self.lecture.theme}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_str = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)

    answer1 = models.CharField(max_length=300, default='')
    answer2 = models.CharField(max_length=300, null=True, blank=True)
    answer3 = models.CharField(max_length=300, null=True, blank=True)
    answer4 = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'Вопрос №{self.id} - Тест №{self.test.lecture.id}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class TestResult(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} - {self.test}'

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'


class Result(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    correctly = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Ответ №{self.id} - {self.question}'

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

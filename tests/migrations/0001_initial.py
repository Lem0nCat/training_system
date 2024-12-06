# Generated by Django 4.1.7 on 2023-04-02 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lectures', '0005_rename_creator_id_lecture_creator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('possible_points', models.IntegerField()),
                ('lecture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='lectures.lecture')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_scored', models.IntegerField()),
                ('date', models.DateField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_str', models.CharField(max_length=300)),
                ('correct_answer', models.CharField(max_length=300)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_str', models.CharField(max_length=300)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
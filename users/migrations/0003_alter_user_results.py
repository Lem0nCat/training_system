# Generated by Django 4.1.7 on 2023-04-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_remove_result_points_scored_remove_result_test_and_more'),
        ('users', '0002_user_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='results',
            field=models.ManyToManyField(through='tests.Result', to='tests.question'),
        ),
    ]
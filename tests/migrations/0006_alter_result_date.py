# Generated by Django 4.1.7 on 2023-04-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_remove_result_points_scored_remove_result_test_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
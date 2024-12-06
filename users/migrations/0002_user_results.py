# Generated by Django 4.1.7 on 2023-04-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_alter_result_options'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='results',
            field=models.ManyToManyField(through='tests.Result', to='tests.test'),
        ),
    ]

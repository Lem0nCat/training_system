# Generated by Django 4.1.7 on 2023-04-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_testresult_user_alter_testresult_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

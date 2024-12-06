# Generated by Django 4.1.7 on 2023-04-03 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0007_testresult_remove_result_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='test',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tests.test'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-02 14:51

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_lecture_show_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
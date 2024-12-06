from django.db import models

from embed_video.fields import EmbedVideoField


class Lecture(models.Model):
    theme = models.CharField(max_length=100)
    show_theme = models.BooleanField(default=True)
    text = models.TextField()
    image = models.ImageField(upload_to='lectures_images')
    video_url = EmbedVideoField(null=True, blank=True)
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.theme
    
    def get_absolute_url(self):
        return f'/lectures/{self.id}'

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'


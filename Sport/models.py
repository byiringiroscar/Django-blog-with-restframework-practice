from django.db import models
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class Statistic(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    goals = models.IntegerField()
    assists = models.IntegerField()
    player_image = models.ImageField(blank=True, null=True, upload_to='images/')
    posted = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Statistic"
        ordering = ['id']


class Comment(models.Model):
    post = models.ForeignKey(Statistic, related_name="comments", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post, self.name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

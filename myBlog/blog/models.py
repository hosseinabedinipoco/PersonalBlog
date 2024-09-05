from django.db import models
from users.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, null=False)
    date = models.DateField()
    view = models.SmallIntegerField(default=0)
    view_user = models.ManyToManyField(User, related_name='articles_viewed')
    wirter = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='articles_written')

class Comment(models.Model):
    content = models.CharField(max_length=100, null=False)
    user = models.ManyToManyField(User)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)    
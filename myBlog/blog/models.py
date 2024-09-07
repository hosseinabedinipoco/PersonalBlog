from django.db import models
from users.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, null=False)
    date = models.DateField()
    content = models.CharField(max_length=500, null=False, default="tt")
    view = models.SmallIntegerField(default=0)
    wirter = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='articles_written')

class Comment(models.Model):
    content = models.CharField(max_length=100, null=False)
    send_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)    
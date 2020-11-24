from django.db import models
from account.models import Account 
from news.models import News

# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("publish",)

    
from django.db import models
from account.models import Account 
from news.models import News
from mptt.models import MPTTModel, TreeForeignKey





class Comment(MPTTModel):

    article = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    # Natural order of the data in the tree
    class MPTTMeta:
        order_insertion_by = ['publish']

    # represent a comment as the return string 
    def __str__(self):
        return f"Comment by {self.account.username}"
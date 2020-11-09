from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=400)
    content = models.TextField(max_length=10000)
    date = models.DateField()
    category = models.ForeignKey('Category', null=True, blank=True,on_delete=models.DO_NOTHING )
    image = models.ImageField(null=True, blank=True, upload_to="gallery")

    

    def __str__(self):
        return self.title

    def get_cat_list(self):
        k = self.category
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:

        #enforcing that there can not be two categories under a parent with same slug
        # __str__ method elaborated later in post.  use __unicode__ in place of
        # __str__ if you are using python 2
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     
    
    def get_news(self):
        return News.objects.filter(category=self)

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

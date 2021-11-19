from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



TYPES=(
    ('fulltime','full time'),
    ('parttime','part time'),
)

class Jobs(models.Model):
    addman=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField( max_length=30)
    job_type=models.CharField(max_length=15 ,choices=TYPES)
    description=models.TextField(max_length=50)
    num_positon=models.IntegerField(default=1)
    #location
    date_join=models.DateTimeField( auto_now=True)
    image=models.ImageField(upload_to='job/',blank=True, null=True)
    category=models.ForeignKey('Category', on_delete=models.CASCADE ,blank=True, null=True)
    salary=models.IntegerField(default=1)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args ,**kwargs):
        self.slug = slugify(self.title)
        super(Jobs,self).save(*args , **kwargs)
    
    def __str__(self):
        return self.title
        

        
class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
class Aplay(models.Model):
    job=models.ForeignKey(Jobs, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=200)
    website=models.URLField( max_length=200)
    load_cv=models.FileField(upload_to=None, max_length=100)
    note=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
    

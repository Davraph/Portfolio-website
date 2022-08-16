from email.policy import default
from tkinter import PhotoImage
from django.db import models
from django.contrib.auth.models import User




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image = models.ImageField(upload_to="posts", null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    views= models.IntegerField(default=0)
    
    def get_absolute_url(self):
         return reverse('post-details', kwargs={"id": self.id})

    # An alternative to use to update the view count 
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.CharField(max_length=120)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
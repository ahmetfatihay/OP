from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    #post_date_edit = models.DateTimeField(auto_now=True, verbose_name="date edited")
    category = models.CharField(max_length=255, default='unlisted')
    snippet = models.CharField(max_length=255, default='go to post')
    likes = models.ManyToManyField(User, related_name='blog_post')
    

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.header_image.delete(save=False)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return '%s - %s' % (self.post.title, self.name)
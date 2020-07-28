from django import forms
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(blank=True,null=True)
    published_date = models.DateTimeField(blank=True,null=True)

    widgets = {
        'title': forms.TextInput(attrs={'class':'textinputclass'}),
        'text': forms.Textarea(attrs = {'class':'editabe medium-editor- postcontent'})
    }

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})    

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    approved_comments = models.BooleanField(default = False)

    widgets = {
        'author': forms.TextInput(attrs={'class':'textinputclass'}),
        'text': forms.Textarea(attrs = {'class':'editabe medium-editor-textarea'})
    }

    def approve(self):
        self.approved_comments=True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
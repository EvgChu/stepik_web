from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')


class Question(models.Model):
    # Question - 
    objects = QuestionManager() 
    # title - 
    title = models.CharField(max_length=255)
    # text - 
    text = models.TextField()
    # added_at - 
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    # rating - 
    rating = models.IntegerField()
    # author - 
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # likes - 
    likes = models.ManyToManyField(User, related_name='question_like_user')
    
    
class Answer(models.Model):
    # Answer - 
    # text - 
    text = models.TextField()
    # added_at - 
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    # question - 
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    # author - 
    aauthor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return super(QuestionManager, self).get_queryset().order_by('-id')
    def popular(self):
        return super(QuestionManager, self).get_queryset().annotate(models.Count('likes')).order_by('likes__count')


class Question(models.Model):
    title = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True)

    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')


    objects = QuestionManager()

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField(max_length=255, default='')
    added_at = models.DateTimeField(auto_now_add=True)

    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text    
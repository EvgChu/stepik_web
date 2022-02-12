from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')


class Question(models.Model):
    # Question - вопрос
    objects = QuestionManager() 
    # title - заголовок вопроса
    title = models.CharField(max_length=255)
    # text - полный текст вопроса
    text = models.TextField()
    # added_at - дата добавления вопроса
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    # rating - рейтинг вопроса (число)
    rating = models.IntegerField()
    # author - автор вопроса
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # likes - список пользователей, поставивших "лайк"
    likes = models.ManyToManyField(User, related_name='question_like_user')
    
    
class Answer(models.Model):
    # Answer - ответ
    # text - текст ответа
    text = models.TextField()
    # added_at - дата добавления ответа
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    # question - вопрос, к которому относится ответ
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    # author - автор ответа
    aauthor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    
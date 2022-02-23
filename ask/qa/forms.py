 
from django import forms

from qa.models import Question, Answer
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',"password")



class AskForm(forms.ModelForm):
    # title = forms.CharField(max_length=255)
    # text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Question
        fields = ('title', 'text',)

class AnswerForm(forms.ModelForm): 
    # text = forms.CharField(widget=forms.Textarea)
    # question = forms.CharField(widget=forms.NumberInput)
    class Meta:
        model = Answer
        fields = ('text',"question")
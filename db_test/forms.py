from django import forms
from django.forms import ModelForm
from .models import Topic


class FormCreateUser(forms.Form):
    first_name = forms.CharField(
        min_length=1, max_length=20, label='Имя', initial='Noname', help_text='Введите имя')
    last_name = forms.CharField(
        min_length=1, max_length=20, label='Фамилия', initial='Noname', help_text='Введите Фамилию')


class FormCreateBlog(forms.Form):
    title = forms.CharField(max_length=255)


class FormCreateTopic(ModelForm):
   class Meta:
       model = Topic
       fields = ('title', 'blog', 'author')

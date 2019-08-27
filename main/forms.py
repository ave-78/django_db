from django import forms

class Form1(forms.Form):
    name = forms.CharField(
        min_length=1, max_length=20, label='Имя', initial='Noname', help_text='Введите свое имя')
    age = forms.IntegerField(
        required=False, min_value=1, max_value=120, label='Возраст', initial='18', help_text='Введите свой возраст')
    email = forms.EmailField(min_length=6, max_length=20, required=False)
    weight = forms.DecimalField(required=False, min_value=4, max_value=250, decimal_places=2)
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)

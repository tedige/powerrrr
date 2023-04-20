from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Имена участников')
    description = forms.CharField(label='Google Disk')
    cost = forms.CharField(label='Номер лидера команды')
    class Meta:
        model = Post
        fields = ('title', 'description','cost',)

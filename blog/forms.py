#coding:utf-8
from django.forms import ModelForm
from blog.models import Article
from django import forms

class ArticleCreationForm(ModelForm):
    title = forms.CharField(error_messages={'requird':'title empty'})
    content = forms.CharField(widget=forms.Textarea, error_messages={'requird':'content empty'})
    class Meta:
        model = Article
        fields = ("title","content")
    
    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args,**kwargs)
    
    def save(self, commit=True):
        article = super().save(commit=False)
        article.author = self.user
        if commit:
            article.save()
        return article

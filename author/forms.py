#coding:utf-8
from django.forms import ModelForm
from author.models import XyUser
from django import forms

class XyUserCreationForm(ModelForm):
    error_messages = {
        'duplicate_username':u'此用户名已存在',
        'password_mismatch':u'两次密码不相等',
        'duplicate_email':u'此email已存在',
    }
    username = forms.RegexField(max_length=30, regex=r'^[\w.@+-]+$',
            error_messages = {
                'invalid':u"用户名智能包含字母数字和@/./+/-",
                'requird':u"用户名未填写",})
    email = forms.EmailField(error_messages={
        'invalid':u"email格式错误",
        'requird':u"email未填写",})
    password1 = forms.CharField(widget=forms.PasswordInput,
            error_messages={
                'requird':u"密码未填写"})
    password2 = forms.CharField(widget=forms.PasswordInput,
            error_messages={
                'requird':u"确认密码未填写"})

    class Meta:
        model = XyUser
        fields = ("username", "email")
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
           XyUser._default_manager.get(username=username)
        except XyUser.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages["duplicate_username"]
        )

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"]
            )
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            XyUser._default_manager.get(email=email)
        except XyUser.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_emil']
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

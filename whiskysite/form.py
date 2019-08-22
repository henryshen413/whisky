import re

from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template.defaultfilters import filesizeformat, slugify
from django.utils.translation import ugettext, ugettext_lazy as _


class CustomAuthenticationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    form_info = {
        'email': '電子信箱',
        'password': '密碼'
    }

    error_messages = {
        'invalid_login': _("電子信箱或密碼錯誤"),
        'inactive': _("電子信箱或密碼錯誤"),
    }

    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, request=None, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if max(enumerate(iter(self.fields)))[0] != field:
                self.fields[field].required = True
                self.fields[field].label = self.form_info[field]
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    "placeholder": "請輸入" + self.form_info[field]
                })
                self.fields[field].error_messages.update({
                    "required": "必填欄位"
                })
            self.fields['email'].error_messages.update({"invalid": "請輸入合法的電子信箱"})
    
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            UserModel = get_user_model()
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                self.user_cache = None
            else:
                if user.check_password(password):
                    self.user_cache = user
                else:
                    self.user_cache = None

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class CustomUserCreationForm(UserCreationForm):
    form_info = {
        'email': '電子信箱',
        'password1': '密碼',
        'password2': '確認密碼',
    }

    error_messages = {'password_mismatch': _("密碼不一致")}
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'此信箱已被註冊使用')
        return email

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if max(enumerate(iter(self.fields)))[0] != field:
                self.fields[field].required = True
                self.fields[field].label = self.form_info[field]
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    "placeholder": "請輸入" + self.form_info[field]
                })
                self.fields[field].error_messages.update({
                    "required": "必填欄位"
                })
        self.fields['password2'].widget.attrs.update({"placeholder": "再次確認密碼"})
    
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
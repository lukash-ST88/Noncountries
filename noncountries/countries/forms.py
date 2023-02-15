from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Country


class OrderingForm(forms.Form):
    ordering = forms.ChoiceField(label='Сортировка по году образования', required=False,
                                 choices=[['year', 'по-возрастанию'], ['-year', 'по-убыванию']],
                                 widget=forms.Select(attrs={'class': 'sort-input'}))


class AddCountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
        self.fields['capital'].empty_label = "Столица не выбрана"

    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'original_name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input-area'}),
            'reasons': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input-area'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'area': forms.NumberInput(attrs={'class': 'form-input'}),
            'population': forms.NumberInput(attrs={'class': 'form-input'}),
            'cat': forms.Select(attrs={'class': 'form-input'}),
            'capital': forms.Select(attrs={'class': 'form-input'}),
            'language': forms.SelectMultiple(attrs={'class': 'form-input'}),
            'year': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_name(self):
        print(self.cleaned_data['name'])
        name = self.cleaned_data['name']
        if type(name) != str:
            raise ValidationError('Имя должно быть строкой')
        name = name.split()
        valid_name = []
        for w in name:
            if w != w.upper() and w != 'и':
                w = w[0].upper() + w[1:]
            if w == 'И':
                w = w.lower()
            valid_name.append(w)
        return " ".join(valid_name)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

from django import forms
from .models import Country

class AddCountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
        self.fields['capital'].empty_label = "Столица не выбрана"

    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'reasons': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

from django import forms
from .models import FAQModel

class FAQModelForm(forms.ModelForm):
    class Meta:
        model = FAQModel
        fields = '__all__'
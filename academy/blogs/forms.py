from django import forms
from .models import BlogUserModel

class BlogUserModelForm(forms.ModelForm):
	class Meta:
		model=BlogUserModel
		fields=['title','image','text']
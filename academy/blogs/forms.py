from django import forms
from .models import BlogModel

class BlogUserModelForm(forms.ModelForm):
	class Meta:
		model=BlogModel
		fields=['title','category_blog','image','text']
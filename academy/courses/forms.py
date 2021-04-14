from django import forms
from .models import CommentCourse, ReplyCommentCourse


class CommentSave(forms.ModelForm):

    class Meta:
        model=CommentCourse
        fields=['text']

class ReplySave(forms.ModelForm):
    class Meta:
        model = ReplyCommentCourse
        fields = ['text']

"""
Forum App Form classes including Thread and Comment Forms
"""
from django import forms
from .models import Thread, Comment


class ThreadForm(forms.ModelForm):
    """
    Form to add and edit threads.
    """
    class Meta:
        """
        To change the behavior of the Thread modal fields
        """
        model = Thread
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):
    """
    Form to add and edit comments.
    """
    class Meta:
        """
        To change the behavior of the Comment modal fields
        """
        model = Comment
        fields = ('post',)
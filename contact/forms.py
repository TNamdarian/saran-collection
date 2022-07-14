# Credit: https://docs.djangoproject.com/en/3.2/topics/forms/

from django import forms


class ContactForm(forms.Form):
    """
    Contact form
    """
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ['email', 'name', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting placeholders on fields
        placeholders = {
            'email': 'Email',
            'name':  'Name',
            'message': 'Message'
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

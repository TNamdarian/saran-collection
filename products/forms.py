from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Origin


class ProductForm(forms.ModelForm):
    """
    Product Form to render the fields in the form for products.
    """
    class Meta:
        """
        Selecting the fields to use.
        """
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        origins = Origin.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_origin = [(o.id, o.get_friendly_name()) for o in origins
                                 ]
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['origin'].choices = friendly_names_origin
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ''

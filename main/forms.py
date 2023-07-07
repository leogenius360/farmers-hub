
from django import forms

from . models import Store


class BusinessRegistrationForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = (
            'name', 'short_desc', 'long_desc',
            'img', 'store_type', 'owner',
        )
        widgets = {
            'store_type': forms.RadioSelect,
            'short_desc': forms.Textarea({'class': 'input', "rows":3, 'placeholder': 'Short description',}),
            'long_desc': forms.Textarea({'class': 'input', 'rows':10, 'placeholder': 'Detail description',}),
        }

    def __init__(self, *args, **kwargs):
        super(BusinessRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'placeholder': 'Name of business',
            'class': 'input',
        })
        self.fields["img"].widget.attrs.update({
            'placeholder': 'Store logo',
            'class': 'input',
        })


from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField, BaseInlineFormSet

from main.models import Product, Contact, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        blacklist = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = self.cleaned_data['name'] + self.cleaned_data['description']

        for b_word in blacklist:
            if b_word in cleaned_data:
                raise forms.ValidationError(
                    'Нельзя использовать запретки (ладно, можно, но не все)')

        else:
            return self.cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published',)


class ContactForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class VersionFormSet(BaseInlineFormSet):

    def clean(self):
        active_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_activе'):
                active_count += 1
        if active_count > 1:
            raise ValidationError("Может существовать только одна активная версия")
        super().clean()

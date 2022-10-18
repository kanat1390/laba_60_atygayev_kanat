from django import forms
from shopapp.models import Order


class ContactForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'phone_number', 'address')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-3', 'style': 'width:400px;', 'placeholder': 'Введите Ваше имя'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mt-3', 'style': 'width:400px;', 'placeholder': 'Введите номер телефона'}),
            'address': forms.Textarea(attrs={'class': 'form-control mt-3', 'style': 'width:400px;', 'placeholder': 'введите адрес для доставки'})
        }

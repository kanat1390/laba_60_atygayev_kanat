from django import forms
from shopapp.models import Product
from searchview.forms import SearchForm


class ProductSearchForm(SearchForm):
    name__icontains = forms.CharField(
        max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Найти...'}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image',
                  'category', 'in_stock', 'price')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'in_stock': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

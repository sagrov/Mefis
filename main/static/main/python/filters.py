import django_filters
from django import forms
from main.models import Product


class ProductFilter(django_filters.FilterSet):
    categories = django_filters.MultipleChoiceFilter(choices=Product.category, widget=forms.CheckboxSelectMultiple()),
    subcategories = django_filters.MultipleChoiceFilter(choices=Product.subcategory, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'subcategory': ['exact']
        }

from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock"]

    def clean_name(self):
        product_name = self.cleaned_data["name"]
        return strip_tags(product_name)

    def clean_description(self):
        product_description = self.cleaned_data["description"]
        return strip_tags(product_description)
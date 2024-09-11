from django import forms

from catalog.models import Product

FORBIDDEN_WORDS = ["казино",
                   "криптовалюта",
                   "крипта",
                   "биржа",
                   "дешево",
                   "бесплатно",
                   "обман",
                   "полиция",
                   "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in FORBIDDEN_WORDS:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError(
                    "Название и описание продукта не должны содержать запрещенные слова"
                )

from django import forms

from catalog.models import Product, Version

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    """Класс для создания форм продукта"""

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


class VersionForm(forms.ModelForm):
    """Класс для создания форм версий продукта"""

    class Meta:
        model = Version
        fields = "__all__"

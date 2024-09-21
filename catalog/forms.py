from django import forms
from django.forms import BooleanField

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


class StyleFormMixin:
    """Миксин для стилизации формы"""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for fild_name, field in self.fields.items():
    #         if isinstance(field, BooleanField):
    #             field.widget.attrs["class"] = "custom-check-input"
    #         else:
    #             field.widget.attrs["class"] = "form-control"
    pass


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Класс для создания форм продукта"""

    class Meta:
        model = Product
        exclude = ("owner",)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in FORBIDDEN_WORDS:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError(
                    "Название и описание продукта не должны содержать запрещенные слова"
                )


class VersionForm(StyleFormMixin, forms.ModelForm):
    """Класс для создания форм версий продукта"""

    class Meta:
        model = Version
        fields = "version_number", "name", "is_current_version"

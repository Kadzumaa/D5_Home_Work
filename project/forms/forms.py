from django import forms
from .models import Inform, Category
from django.core.exceptions import ValidationError


class NA_Form(forms.ModelForm):
    class Meta:
        model = Inform
        fields = ['name', 'description', 'category']

        labels = {
            'name': 'Название',
            'description': 'Описание',
            'category': 'Категория',
        }

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if description is not None and len(description) < 20:
            raise ValueError({
                "description": "Описание не может быть менее 20 символов"
            })

        name = cleaned_data.get('name')
        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию"
            )

        return cleaned_data

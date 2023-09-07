from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput, ModelChoiceField, MultipleChoiceField, CharField
from .models import Inform, Category

class InformsFilter(FilterSet):
    # name_post = ModelChoiceField(queryset=Inform.objects.all(), empty_label='Название', label='Имя')
    # description_post = CharField(max_length=255, label='Текст')
    # category_post = MultipleChoiceField(queryset=Category.objects.category, label='Категория')
    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
        model = Inform
        fields = {'name': ['icontains'], 'category': ['exact']}


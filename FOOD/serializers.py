from rest_framework import fields, serializers
from .models import Type_choices, Size_choices

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    pizza_type = fields.MultipleChoiceField(choices=Type_choices)
    pizza_size = fields.MultipleChoiceField(choices=Size_choices)
        
from django.db import models
from multiselectfield import MultiSelectField
# from django.utils.encoding import python_2_unicode_compatible
from django.utils.six import python_2_unicode_compatible
# from six import python_2_unicode_compatible

# Create your models here.~

Type_choices = (
        ('Regular', 'Regular Pizza'), ('Square', 'Square Pizza')
    )
    
Size_choices = (
    ('S', 'Small'),('M', 'Medium'),('L', 'Large')
)

Topping_selection = (
    ('onion', 'Onion'),('tomato', 'Tomato'),('corn', 'Corn'),('capsicum', 'Capsicum'),('cheese', 'Cheese'),('jalapeno', 'Jalapeno')
)

@python_2_unicode_compatible
class Pizza(models.Model):
    pizza_type = models.CharField(max_length = 100, choices = Type_choices)
    pizza_size = models.CharField(max_length = 100, choices = Size_choices)
    pizza_topping = MultiSelectField(choices = Topping_selection)

    
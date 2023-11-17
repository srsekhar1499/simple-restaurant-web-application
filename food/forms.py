from django import forms
from django.forms import TextInput
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        widgets = {
            'item_name' : TextInput(attrs={
                'class' : 'form-control',
                'style' : 'max_width=300px',
                'placeholder' : 'Item Name'
            }),
            
            'item_desc' : TextInput(attrs={
                    'class' : 'form-control',
                    'style' : 'max_width=300px',
                    'placeholder' : 'Item description'
            }),

            'item_price' : TextInput(attrs = {
                'class' : 'form-control',
                'style' : 'max_width=300px',
                'placeholder' : 'Price'
            })
            }
        

"""

'item_name': TextInput(
                    attrs = {
                        
                    }
                ),
            'item_desc' : TextInput(attrs={
                    'class' : 'form-control',
                    'style' : 'max_width=300px',
                    'placeholder' : 'Item description'
                }),

            'item_price' : TextInput(attrs = {
                        'class' : 'from-control',
                        'placeholder' : 'Price'
                        'style' : 'max_width=300px',
                    }
                )

"""
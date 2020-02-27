from django import forms
from .models import Producto, Categoria, Usuario

class ProForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'fkCategoria']
        labels= {'nombre': 'nombre de producto', 'precio':'precio' ,'descripcion': 'descripción', 'fkCategoria': 'categoría'}
        
        widgets={
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'nombre'
            }
            ),
            'precio': forms.NumberInput(
                attrs={'class': 'form-control',
                 'id': 'precio'
                 }),
            'descripcion': forms.TextInput(
                attrs={'class':'form-control',
                'id':'descripcion',
                'placeholder':'texto para ver'
                }
            ),
            'fkCategoria': forms.Select(
                attrs={'class':'form-control',
                'id':'fkCategoria'
                }
            )

        }

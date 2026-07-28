from django import forms
from django.core import validators

class FormularioArticle(forms.Form):

    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder':'Mete el titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, "El titulo es demasiado corto"),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', "El titulo esta mal formado",'invalid_title') # Solo letra y numero 
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea,
        validators = [
            validators.MaxLengthValidator(20, 'Te has pasado de caracteres maximo 20 caracteres de contenido'),
            
        ]
    )
    content.widget.attrs.update({
        'placeholder':'Mete el contenido del articulo completo',
        'class': 'contenido_form_article',
        'id':'conteido_form_id',
    })

    public_options = [
        (1, "Si"),
        (0, "No")
    ]
    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices= public_options
    ) 
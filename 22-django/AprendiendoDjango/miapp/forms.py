from django import forms

class FormularioArticle(forms.Form):

    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=False,
        widget= forms.TextInput(
            attrs={
                'placeholder':'Mete el titulo',
                'class': 'titulo_form_article'
            }
        )
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea
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
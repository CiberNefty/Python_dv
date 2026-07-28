from django import forms

class FormularioArticle(forms.Form):

    title = forms.CharField(
        label="Titulo"
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea
    )

    public_options = [
        (1, "Si"),
        (0, "No")
    ]
    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices= public_options
    ) 
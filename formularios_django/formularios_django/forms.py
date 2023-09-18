from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre",max_length=100, help_text="100 caracteres como max")
    url = forms.URLField(label="Tu sitio web", required=False)
    comment = forms.CharField()
    
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre:", max_length=10, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", max_length=10, widget=forms.EmailInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={"class": "form-control"}))
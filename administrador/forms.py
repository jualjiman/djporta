from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': '¿Cuál es tu nombre?','class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '¿Cuál es tu email?','class':'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '¿En qué te puedo ayudar?','class':'form-control'}))
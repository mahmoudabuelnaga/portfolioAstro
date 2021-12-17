from django import forms
from django.forms import widgets

class ContatUS(forms.Form):
    name    = forms.CharField(widget=forms.TextInput(attrs={
        'name':'name',
        'type':'text',
        'class':'form-control rounded-0 border-top-0 border-end-0 border-start-0',
        'placeholder':'Name',
    }))
    email   = forms.EmailField(widget=forms.EmailInput(attrs={
        'name':'email', 
        'type':'text', 
        'class':'form-control rounded-0 border-top-0 border-end-0 border-start-0', 
        'placeholder':'Email',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'5', 
        'name':'message', 
        'class':'textarea form-control rounded-0 border-top-0 border-end-0 border-start-0', 
        'placeholder':'Message',
    }))

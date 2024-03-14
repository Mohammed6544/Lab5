from django import forms

class PersonForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
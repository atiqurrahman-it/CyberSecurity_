from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Contact

#
# class Contact_Form(forms.Form):
#     name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Type your name',
#
#     }))
#     email = forms.EmailField(label='', required=True, widget=forms.TextInput(attrs={
#         'placeholder': 'Type your email',
#         'type': 'email',
#         'class': 'form-control',
#     }))
#     subject = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Type your subject',
#
#     }))
#     details = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control',
#                                                                      'rows': 8,
#                                                                      'placeholder': 'Type your Message'
#                                                                      }
#                                                               ))

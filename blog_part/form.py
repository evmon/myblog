from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Comment


class CommentForm(forms.ModelForm):
	
	class Meta():

		model = Comment
		fields = ['author','text',]
		widgets = {
			'author': forms.TextInput( attrs={'class':'form-control', 'label':'Your name',}),
			'text': forms.TextInput( attrs={'class':'form-control', 'label':'Your message',}),
 			}
       

# class InputForm(forms.ModelForm):
#     class Meta:
#         form_class = AuthenticationForm
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={'autofocus': '','placeholder':'Username', 'class':'form-control'}),
#             'password': forms.PasswordInput(attrs={'autofocus': '','placeholder':'Password', 'class':'form-control'}),
#         }
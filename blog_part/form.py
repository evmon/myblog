from django import forms

from .models import Post


class PostForm(forms.ModelForm):

	# title = forms.CharField(       
 #        widget=forms.PasswordInput(attrs={'placeholder':'Title', 'class':'form-control'}),
 #      )
 #    text = forms.TextInput(
 #        widget=forms.PasswordInput(attrs={'placeholder':'Enter the same text.', 'class':'form-control'}),
 #      )
    class Meta:
        model = Post
        widget=forms.TextInput(attrs={'class':'form-control'}),
        fields = ['title','text',]
       


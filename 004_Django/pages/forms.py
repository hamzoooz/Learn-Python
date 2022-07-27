from django import forms
from .models import Login

class LoginForm(forms.ModelForm):

    class Meta:
        model  = Login
        fields = '__all__'
        # fields = ['username']
    # username = forms.CharField(max_length=50, requird=True)
    # username2 = forms.CharField(max_length=50 )
    # password2 = forms.CharField(max_length=50, widget=forms.PasswordInput)

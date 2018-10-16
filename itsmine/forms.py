from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Member_Details

CHOICES=(('Mr','Mr.'),('Mrs','Mrs.'))
Date_Choices=[x for x in range(1990,2030)]

class RegForm(forms.ModelForm):
    class Meta:
        model=Member_Details
        widgets={'password':forms.PasswordInput(attrs={'placeholder':'Password'}),'title':forms.Select(choices=CHOICES),
                 'DOB':forms.SelectDateWidget(years=Date_Choices),
                 'first_Name':forms.TextInput(attrs={'placeholder':'Enter First name'}),
                 'last_Name': forms.TextInput(attrs={'placeholder': 'Enter Last name'}),
                 'email': forms.EmailInput(attrs={'placeholder': 'Enter Email Id'}),
                 'username': forms.TextInput(attrs={'placeholder': 'Username'}),}
        fields=['title','first_Name','last_Name','username','password','email','DOB']
    def clean(self):
        data=super(RegForm,self).clean()
        username=Member_Details.objects.filter(username=data.get('username'))
        email=Member_Details.objects.filter(email=data.get('email'))
        if username:
            raise forms.ValidationError('Username is already taken')
        elif email:
            raise forms.ValidationError('Account is already existed with this Email Id')

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,
                             widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



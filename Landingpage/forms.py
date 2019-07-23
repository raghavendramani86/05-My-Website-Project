from django import forms
from Landingpage.models import Details, Profile
from django.contrib.auth.models import User

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('website','picture')

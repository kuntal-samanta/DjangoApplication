from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 
 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'email']
 
 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




"""
    Model Form

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class PartialAuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ['title']

"""


"""
    Normal Form

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    recipients = MultiEmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean(self):
        super(ContactForm).clean()
        cc_myself = self.cleaned_data.get("cc_myself")
        subject = self.cleaned_data.get("subject")

        if cc_myself and subject and "help" not in subject:
            msg = "Must put 'help' in subject when cc'ing yourself."
            self.add_error('cc_myself', msg)
            self.add_error('subject', msg)

        return self.cleaned_data

"""


# https://www.educative.io/answers/how-to-do-django-form-validation


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    national_id = forms.CharField(max_length=15, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    date_of_birth = forms.DateField(required=True)

    class Meta:
        model = User
        fields = (
        'username', 'national_id', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserProfileCreationForm, self).save(commit=False)
        user_profile = UserProfile(
            user=user,
            national_id=self.cleaned_data['national_id'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            date_of_birth=self.cleaned_data['date_of_birth']
        )
        if commit:
            user_profile.save()
            user.save()
        return user, user_profile

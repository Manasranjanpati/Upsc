from django import forms
from User.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class ChangePasswordForm(forms.Form):
    Newpassword = forms.CharField(max_length=100)
    confirm = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_confirm(self):
        if self.data.get('confirm') != self.cleaned_data.get('Newpassword'):
            raise forms.ValidationError(
                'Confirm password do not match with new password')
        # password_validation.validate_password(
        #     self.cleaned_data.get('Newpassword'), user=self.user)
        self.user.set_password(self.cleaned_data.get('confirm'))
        return self.data.get('confirm')

    def save(self):
        self.user.set_password(self.cleaned_data.get('confirm'))
        self.user.save()
        return self.user

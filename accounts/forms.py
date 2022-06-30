from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

USER = get_user_model()

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
                                    widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'New Password'
            }))
    new_password2 = forms.CharField(
                                    widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm New Password'
            }))


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }), max_length=254)



class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }))

    class Meta:
        model = USER
        fields = (
            'first_name',
            'last_name',
            'email',
            'image',
            'username',
            'password',
            'confirm_password'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Image'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            })
        }

    def clean(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("Password and confirm_password does not match")
        return super().clean()


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Old Password'
                                    }))
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'Confirm Password'}))


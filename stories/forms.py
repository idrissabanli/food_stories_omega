from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from stories.models import Contact, Story
from stories.validators import validate_gmail_account

class ContactForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_gmail_account, ], max_length=40, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    # name = forms.CharField(widget=)
    # message = forms.CharField(widget=)

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     if not cleaned_data['email'].endswith('@gmail.com'):
    #         raise forms.ValidationError('Email gmail account olmalidir')
    #     return super().clean()
    
    # def clean_email(self):
    #     cleaned_data = self.cleaned_data
    #     if not cleaned_data['email'].endswith('@gmail.com'):
    #         raise forms.ValidationError('Email gmail account olmalidir')
    #     return True


    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Your name'
            }),
            'message': forms.Textarea(attrs={
                'rows': 10,
                'class': 'form-control',
                'placeholder': 'Message'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control',
            })
        }


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = (
            'title',
            'category',
            'image',
            'cover_image',
            'content',
            'tags',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'placeholder': 'Category',
                'class': 'form-control'
            }),
            'image': AdminFileWidget(attrs={
                'placeholder': 'Image',
                'class': 'form-control'
            }),
            'cover_image': AdminFileWidget(attrs={
                'placeholder': 'Cover image',
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Content',
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'placeholder': 'tags',
                'class': 'form-control'
            }),
            # 'author': forms.Select(attrs={
            #     'placeholder': 'Author',
            #     'class': 'form-control'
            # }),
        }
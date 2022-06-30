from django.core.exceptions import ValidationError


def validate_gmail_account(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Email sehvdir')
    return True
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_password_pair(password, commit_password):
    if password != commit_password:
        raise ValidationError(
            {'commit_password': _('Password and commit_password are not equal')},
            'password_mismatch',
        )

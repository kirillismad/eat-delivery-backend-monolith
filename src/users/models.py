from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import CASCADE
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from rest_framework.utils.formatting import lazy_format


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(username, password, **extra_fields)

    def create(self, *args, **kwargs):
        raise RuntimeError('Don\'n user `.create` method for UserManager')


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(_('email'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active.'),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return lazy_format(_('User: {email}'), email=self.email)

    def __repr__(self):
        return f'User(pk={self.pk}, email={self.email})'


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, primary_key=True, verbose_name=_('user')
    )
    name = models.CharField(_('name'), max_length=64)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    @cached_property
    def email(self):
        # noinspection PyUnresolvedReferences
        return self.user.email

    def __str__(self):
        return lazy_format(_('Profile: {email}, {name}'), email=self.email, name=self.name)

    def __repr__(self):
        return f'Profile(pk={self.pk}, email={self.email}, name={self.name})'

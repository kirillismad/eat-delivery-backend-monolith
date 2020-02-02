from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import get_error_detail

from users.models import User, Profile
from users.validators import validate_password_pair


class PasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        kwargs['write_only'] = True
        kwargs['style'] = {'input_type': 'password'}
        super().__init__(**kwargs)


class UserSerializer(serializers.ModelSerializer):
    password = PasswordField()
    commit_password = PasswordField()

    class Meta:
        model = User
        fields = ['email', 'password', 'commit_password']

    def validate_password(self, password):
        try:
            validate_password(password)
        except DjangoValidationError as e:
            raise ValidationError(get_error_detail(e), 'invalid_password_validation')
        return password

    def validate(self, attrs):
        commit_password = attrs.pop('commit_password')
        try:
            validate_password_pair(attrs['password'], commit_password)
        except DjangoValidationError as e:
            raise ValidationError(get_error_detail(e), e.code)
        return attrs


class SignUpSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        return Profile.objects.create(
            user=User.objects.create_user(**user_data),
            **validated_data
        )

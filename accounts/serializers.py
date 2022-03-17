import pdb

from asyncore import write
from pyexpat import model

from .models import User
from .utils import Util

from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse

from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length = 16,
        min_length = 8,
        write_only = True,
    )

    class Meta:
        model = User
        fields = [
            'email',
            'username', 
            'first_name',
            'last_name',
            'password',
        ]

    def validate(self, attrs):
        email = attrs.get(
            'email',
            '',
        )
        username = attrs.get(
            'username', 
            '',
        )
        first_name = attrs.get(
            'firstname', 
            '',
        )
        last_name = attrs.get(
            'lastname', 
            '',
        )

        if not username.isalnum():
            raise serializers.ValidationError("The <b>username</b> should only contain alphanumeric characters!")

        return attrs

    def create(sell, validated_data):
        return User.objects.create_user(**validated_data)

        #user = request.data
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length = 555)

    class Meta:
        model = User
        fields = [
            'token'
        ]

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length = 16, min_length = 8, write_only = True)
    username = serializers.CharField(max_length = 255, min_length = 2, read_only =True)
    tokens = serializers.CharField(max_length = 68, min_length = 8, read_only = True)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'username',
            'tokens'
        ]


    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email = email, password = password)

        #pdb.set_trace()

        if not user:
            raise AuthenticationFailed('Invalid Credentials, Try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        if not user.is_verified:
            raise AuthenticationFailed('Email not verified')
 
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }

        return super().validate[attrs]

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length = 2)

    class Meta:
        fields = ['email']

    # def validate(self, attrs):
    #     email = attrs['data'].get('email', '')
        

    #         return super().validate[attrs]


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length = 8, max_length = 16, write_only = True)
    token = serializers.CharField(min_length = 1, write_only = True)
    uidb64 = serializers.CharField(min_length = 1, write_only=True)

    class Meta:
        fields = [
            'password',
            'token',
            'uidb64',
        ]

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("The reset link is invalid", 401)

            user.set_password(password)
            user.save()
            return (user)

        except Exception as e:
            raise AuthenticationFailed("The reset link is invalid", 401)

        return super().validate(attrs)

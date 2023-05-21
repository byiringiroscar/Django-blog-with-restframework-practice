from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Sport.models import Statistic, Comment


class StatisticSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source="posted.username", read_only=True)
    username = serializers.SerializerMethodField("get_username_from_author")

    class Meta:
        ref_name = "User 2"
        model = Statistic
        fields = ['name', 'position', 'team', 'country', 'description', 'goals', 'assists', 'player_image', 'username']
        read_only_fields = ['posted']

    # def get_username(self, obj):
    #     return obj.posted.username

    def get_username_from_author(self, blog_posted_by):
        username = blog_posted_by.posted.username
        return username


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        user.set_password(password)
        user.save()
        return user


class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email']

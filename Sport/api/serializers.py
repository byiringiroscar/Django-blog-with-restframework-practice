from rest_framework import serializers
from Sport.models import Statistic, Comment


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "User 1"
        model = Statistic
        fields = '__all__'
        read_only_fields = ['posted']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

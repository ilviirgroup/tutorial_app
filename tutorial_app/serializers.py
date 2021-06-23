from rest_framework import serializers
from tutorial_app.models import Category


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
            'course_name',
            'category_name',
            'english',
            'russian',
            'turkmen',
            'turkish',
            'color')
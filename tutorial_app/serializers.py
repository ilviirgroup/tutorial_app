from rest_framework import serializers
from tutorial_app.models import Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id',
            'english',
            'russian',
            'turkmen',
            'turkish')
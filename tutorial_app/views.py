"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.shortcuts import render
from rest_framework import status
from tutorial_app.models import Language
from tutorial_app.serializers import LanguageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def language_list(request):
    if request.method == 'GET':
        toys = Language.objects.all()
        toys_serializer = LanguageSerializer(toys, many=True)
        return Response(toys_serializer.data)
    elif request.method == 'POST':
        toy_serializer = LanguageSerializer(data=request.data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(toy_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def language_detail(request, pk):
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:

        if request.method == 'GET':
            language_serializer = LanguageSerializer(language)
            return Response(language_serializer.data)
        elif request.method == 'PUT':
            language_serializer = LanguageSerializer(language, data=request.data)
            if language_serializer.is_valid():
                language_serializer.save()
                return Response(language_serializer.data)
            return Response(language_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            language.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES,STYLE_CHOICES

class SnippetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__' 
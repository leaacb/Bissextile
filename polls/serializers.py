from rest_framework import serializers
from .models import Archive


class YearSerializer(serializers.Serializer):
    value = serializers.IntegerField()


class RangeYearSerializer(serializers.Serializer):
    first_year = serializers.IntegerField()
    second_year = serializers.IntegerField()


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        exclude = ['id']
        ordering = ['-date']

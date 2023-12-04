from rest_framework import serializers


class YearSerializer(serializers.Serializer):
    value = serializers.IntegerField()


class RangeYearSerializer(serializers.Serializer):
    first_year = serializers.IntegerField()
    second_year = serializers.IntegerField()

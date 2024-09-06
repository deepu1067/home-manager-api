from rest_framework import serializers

class GoogleSheetRowSerializer(serializers.Serializer):
    values = serializers.ListField(
        child=serializers.CharField(), 
        allow_empty=False
    )
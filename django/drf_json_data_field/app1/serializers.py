import json
from rest_framework import serializers

from .models import Model1


class JSONDataField(serializers.Field):
    """JSONテキストのシリアライザ,デシリアライザフィールド
    """
    def to_representation(self, obj):
        if obj:
            return json.loads(obj)
        return None

    def to_internal_value(self, data):
        return json.dumps(data, indent=2)


class Model1Serializer(serializers.ModelSerializer):
    data = JSONDataField()

    class Meta:
        model = Model1
        fields = [
            'id', 'data'
        ]

from rest_framework import serializers
from core.models import Record

class RecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ['id']

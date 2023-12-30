from rest_framework import viewsets, pagination
from rest_framework.response import Response
from .serializers import RecordSerializers
from core.models import Record

class CustomPagination(pagination.PageNumberPagination):
    page_size = 20

class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializers
    queryset = Record.objects.all()
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)

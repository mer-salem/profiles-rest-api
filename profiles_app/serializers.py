from rest_framework import serializers


class SerializerHelloApi(serializers .Serializer):
    name = serializers .CharField(max_length=10)

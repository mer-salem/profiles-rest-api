from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_app import serializers
from rest_framework import status


class HelloApiView(APIView):
    serializer_class = serializers.SerializerHelloApi

    def get(self, request, fomat=None):

        api_list = ['veza', 'omar', 'hemana']
        return Response({'message': api_list})

    def put(self, request, pk=None):
        # return super().put(request, *args, **kwargs)
        return Response({'message': 'put'})

    def patch(self, request, pk=None):
        return Response({'message': 'patch'})

    def delete(self, request, pk=None):
        return Response({'message': 'delete'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

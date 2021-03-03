from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, fomat=None):

        api_list = ['veza', 'omar', 'hemana']
        return Response({'message': api_list})

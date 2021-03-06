from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_app import serializers, models
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from profiles_app import permissions
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ProfileFeedItemViewsets(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    permission_classes = (permissions.UpdateOwnerStatus,
                          IsAuthenticated)
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnerProfile,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'email',)


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


class HelloViewsets(viewsets.ViewSet):

    serializer_class = serializers.SerializerHelloApi

    def list(self, request):
        api_list = ['veza', 'omar', 'hemana']
        return Response({'message': 'hello', 'api_list': api_list})

    def create(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response({'bbbb': 'serializer.errors, status=status.HTTP_400_BAD_REQUEST'})

    def retrive(self, request, pk=None):
        return Response({'message': 'retrive'})

    def update(self, request, pk=None):
        return Response({'message': 'update'})

    def partial_update(self, request, pk=None):
        return Response({'message': 'partial_update'})

    def destroy(self, request, pk=None):
        return Response({'message': 'destroy1'})

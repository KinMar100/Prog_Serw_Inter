from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets

from . models import Rank, User

from .serializers import UserSerializer, AuthTokenSerializer, RankSerializer

# Create your views here.


class CreateUserListView(generics.ListCreateAPIView):
    """Create a new user in the system"""
    queryset = User.object.all()
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    queryset = User.object.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        """Retrieve and return authenticated user"""

        return self.request.user


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class RankListView(generics.ListCreateAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
    permission_classes = (permissions.AllowAny, )




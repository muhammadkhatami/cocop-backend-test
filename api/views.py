from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import User
from api.serializers import UserSerializer
# Also add these imports
from api.permissions import IsLoggedInUserOrAdmin

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]


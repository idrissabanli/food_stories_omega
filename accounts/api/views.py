from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from accounts.api.serializers import UserSerializer

User = get_user_model()


class UserProfileAPIView(RetrieveAPIView):
    """
    This endpoint for get user detail
    """
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

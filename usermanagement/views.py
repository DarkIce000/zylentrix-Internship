from django.contrib.auth import authenticate

from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, mixins, status


from .models import User
from .serializers import UserSerializer


class UserManagementAPIView(
    mixins.CreateModelMixin, 
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    generics.GenericAPIView
    ):
    """
    CRUD Operation on user model. For the security reasons, I have only
    permitted admin user to perform CRUD on the user table.

    Note: CRUD can only be performed by Admin user,
    make sure either you created a superuser or checked a
    existing normal user as staff

    """
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes     = [IsAdminUser]

    queryset         = User.objects.all()
    serializer_class = UserSerializer
    lookup_field     = 'username'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if username:
            return self.retrieve(request, *args, **kwargs)              # retrieve a single user
        return self.list(request, *args, **kwargs)                      # list all the user
    
    def post(self, request, *args, **kwargs):                           # create a user 
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):                            # update 
        username = kwargs.get('username')
        if not username:
            return Response(
                {"detail": "Username is required to update a user."},
                status=status.HTTP_400_BAD_REQUEST
                ) 
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):                          # partial update
        username = kwargs.get('username')
        if not username:
            return Response(
                {"detail": "Username is required to patch a user."}, 
                status=status.HTTP_400_BAD_REQUEST
                ) 
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if not username:
            return Response(
                {"detail": "Username is required to delete a user."},
                status=status.HTTP_400_BAD_REQUEST
                )       
        return self.destroy(request, *args, **kwargs)


class RegisterAPIView(generics.CreateAPIView):
    """
    registeration view
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework import generics

from .serializers import SignUpSerializer


class SignUpView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = SignUpSerializer

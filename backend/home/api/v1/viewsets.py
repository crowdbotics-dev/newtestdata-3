from rest_framework import viewsets
from home.models import Test, Testcheck, Testingsaap, Testnews
from .serializers import (
    TestSerializer,
    TestcheckSerializer,
    TestingsaapSerializer,
    TestnewsSerializer,
)
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class TestingsaapViewSet(viewsets.ModelViewSet):
    serializer_class = TestingsaapSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Testingsaap.objects.all()


class TestnewsViewSet(viewsets.ModelViewSet):
    serializer_class = TestnewsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Testnews.objects.all()


class TestcheckViewSet(viewsets.ModelViewSet):
    serializer_class = TestcheckSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Testcheck.objects.all()


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Test.objects.all()

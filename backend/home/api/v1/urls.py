from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TestViewSet, TestcheckViewSet, TestingsaapViewSet, TestnewsViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("testingsaap", TestingsaapViewSet)
router.register("testnews", TestnewsViewSet)
router.register("testcheck", TestcheckViewSet)
router.register("test", TestViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

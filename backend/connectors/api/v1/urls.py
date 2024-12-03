from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137691ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137691", Testconnectors137691ViewSet, basename="testconnectors137691"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]

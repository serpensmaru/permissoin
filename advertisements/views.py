from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permission import IsAuthenticatedOrReadOnly
from advertisements.serializers import UserSerializer, AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()

    serializer_class = AdvertisementSerializer
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий - с указанием для каких действий конкректно"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # return [IsAuthenticated(), IsAuthenticatedOrReadOnly()]
            return [IsAuthenticatedOrReadOnly()]
            # return [IsAuthenticated()]
        return []



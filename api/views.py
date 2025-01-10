from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datka_app.models import *
from .serializers import *
from .filters import NewsFilter


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = NewsFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the action.
        """
        if self.action == 'list':
            return ListNewsSerializer
        elif self.action == 'retrieve':
            return DetailNewsSerializer
        return ListNewsSerializer  # Default serializer if no action matches


class AdministrationViewSet(ModelViewSet):
    queryset = Adminstration.objects.all()
    lookup_field = "id"
    serializer_class = AdminstrationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class JobsViewSet(ModelViewSet):
    queryset = Jobs.objects.all()
    lookup_field = "id"
    serializer_class = JobsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class EarthViewSet(ModelViewSet):
    queryset = Earth.objects.all()
    lookup_field = "id"
    serializer_class = EarthSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AgriculturalViewSet(ModelViewSet):
    queryset = Agricultural.objects.all()
    lookup_field = "id"
    serializer_class = AgriculturalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class StateLandViewSet(ModelViewSet):
    queryset = StateLand.objects.all()
    lookup_field = "id"
    serializer_class = StateLandSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ResolutionViewSet(ModelViewSet):
    queryset = Resolution.objects.all()
    lookup_field = "id"
    serializer_class = ResolutionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)
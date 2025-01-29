from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datka_app.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
# from .filters import NewsFilter


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_class = NewsFilter
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


class GlavaViewSet(ModelViewSet):
    queryset = Glava.objects.all()
    lookup_field = "id"
    serializer_class = GlavaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AdminsViewSet(ModelViewSet):
    queryset = Admins.objects.all()
    lookup_field = "id"
    serializer_class = AdminSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)



@api_view(["POST"])
def contact_form(request):
    data = request.data

    last_name = data.get("last_name", "")
    first_name = data.get("first_name", "")
    middle_name = data.get("middle_name", "")
    email = data.get("email", "")
    phone = data.get("phone", "")
    address = data.get("address", "")
    subject = data.get("subject", "Без темы")
    message = data.get("message", "")

    if not email or not message:
        return Response({"error": "Email и сообщение обязательны!"}, status=400)

    # Формируем сообщение
    email_subject = f"Новое сообщение от {last_name} {first_name}"
    full_message = (
        f"ФИО: {last_name} {first_name} {middle_name}\n"
        f"Email: {email}\nТелефон: {phone}\nАдрес: {address}\n\n"
        f"Тема: {subject}\nСообщение:\n{message}"
    )

    # Отправляем письмо на Gmail
    send_mail(email_subject, full_message, email, ["oshai4683@gmail.com"])

    return Response({"message": "Сообщение отправлено успешно!"})

from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cars.models import Car, Application
from cars.permisisions import IsOwnerOrReadOnly
from cars.serializers import CarDealerSerializer, CarSerializer, ApplicationSerializer
from django.core.mail import send_mail
from rest_framework.response import Response


def send_application_to_dealer(data, application):
    """
    Функция формирует и отправяет дилеру заявку от клиента на почту
    :param data: информация о заявке
    :param application: объект заявки
    """
    car = Car.objects.get(id=data['car_id'])
    dealer_email = User.objects.get(id=car.dealer_id.id).email
    message = f'Необходимо записать клиента {data["name"]} на тест драйв. id заявки - {data["number"]}. ' \
              f'Заявка номер - {application.id}'
    if data['application_subject'] == 'question':
        message = f'Необходимо проконсультировать клиента {data["name"]} по выбранной модели - {car.model}. ' \
                  f'Номер - {data["number"]}. id заявки - {application.id}'
    send_mail(
        'Заявка от клиента',
        message,
        data['email'],
        [dealer_email]
    )


class CarDealerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CarDealerSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def list(self, request, *args, **kwargs):
        """Дилерам отображаются заявки только по их машинам"""
        if request.user.is_authenticated:
            super().list(request, *args, **kwargs)
            res = Application.objects.filter(dealer_id=request.user.id)
            serializer = ApplicationSerializer(res, many=True)
            return Response({
                "applications": serializer.data
            })
        return Response({
            'error': 'Смотреть список заявок могут только дилеры'
        })

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        dealer_id = Car.objects.get(id=response.data['car_id']).dealer_id.id
        Application.objects.update(dealer_id=dealer_id)
        return response

    def perform_create(self, serializer):
        application = serializer.save()
        data = serializer.data
        send_application_to_dealer(data, application)

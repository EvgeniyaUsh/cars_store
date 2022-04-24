from django.contrib.auth.models import User
from rest_framework import serializers

from cars.models import Car, Application


class CarDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CarSerializer(serializers.ModelSerializer):
    # в скрытом поле по умолчанию прописывается текущий пользователь
    dealer_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ('dealer_id',)

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
CHOICES_APPLICATION_SUBJECT = (
    ('test', 'Тест драйв'),
    ('question', 'Консультация'),
)


class Car(models.Model):
    dealer_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='dealer')
    dealer_name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.model


class Application(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='car')
    dealer_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(validators=[phoneNumberRegex], max_length=16)
    application_subject = models.CharField(max_length=50, choices=CHOICES_APPLICATION_SUBJECT)

    objects = models.Manager()

from django.db import models
from datetime import datetime

# Create your models here.
TYPE_OF_ROOM = {
  ("L", "Люкс"),
  ("M", "Полулюкс"),
  ("S", "Стандарт")
}

PAYMENT_FORM = {
  ("M", "MasterCard"),
  ("V", "Visa"),
  ("C", "Наличный расчет"),
  ("O", "Другое")
}


class Client(models.Model):
  iin = models.CharField(max_length=12)
  last_name = models.CharField(max_length=20)
  first_name = models.CharField(max_length=20)
  father_name = models.CharField(max_length=20)

  class Meta:
    verbose_name = "Клиент"
    verbose_name_plural = "Клиенты"

  def __str__(self):
    return "{} {}".format(self.last_name, self.first_name)


class Reservation(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  estimated_date_in = models.DateTimeField(null=True)
  estimated_date_out = models.DateTimeField(null=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=20)
  type_of_room = models.CharField(max_length=1, choices=TYPE_OF_ROOM, default="S")

  class Meta:
    verbose_name = "Бронирование"
    verbose_name_plural = "Бронирования"

  def __str__(self):
    return "{} {}".format(self.client.last_name, self.client.first_name)


class Transaction(models.Model):
  reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
  date_in = models.DateTimeField(default=datetime.now())
  date_out = models.DateTimeField(null=True)
  payment_form = models.CharField(max_length=1, choices=PAYMENT_FORM, default="O")

  class Meta:
    verbose_name = "Транзакция"
    verbose_name_plural = "Транзакции"

  def __str__(self):
    return "{} {}".format(self.reservation.client.last_name, self.reservation.client.first_name)
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)
    patronymic = models.CharField(max_length=48)
    passport = models.PositiveIntegerField()
    phone_number = models.IntegerField()
    place_of_residence = models.CharField(max_length=72)

    def __str__(self):
        return "Client %s %s" % (self.name, self.surname,)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

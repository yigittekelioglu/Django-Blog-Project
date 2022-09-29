from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.db import models


# class Profile(models.Model):
#   gender = (
#        ('male', 'Male'),
#       ('female', 'Female'),
#    )
#
#        user = models.OneToOneField(User, on_delete=models.CASCADE)
#        birthdate = models.DateField()
#        gender = models.CharField(max_length=10, choices=gender)

class Profile(AbstractUser):
    gender = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    birthdate = models.DateField(null=True, verbose_name='Doğum Tarihi')
    gender = models.CharField(max_length=10, choices=gender, null=True, blank=False, verbose_name='Cinsiyet')

    REQUIRED_FIELDS = ['birthdate', 'gender']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"





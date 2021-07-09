from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

class Client(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    tel_number = models.CharField(max_length=9, validators=[RegexValidator(r'^[0-9]{9}$')], unique=True, null=False)

    CHOICES_HAIR = (
        (1, "Długie"),
        (2, "Pół-długie"),
        (3, "Krótkie"))

    hair = models.PositiveSmallIntegerField(choices=CHOICES_HAIR, blank=True)


    def __str__(self):
        stel = str(self.tel_number)
        space_tel = stel[0:3] + " " + stel[3:6] + " " + stel[6:9]
        return self.first_name + " " + self.last_name + " " + "(" + space_tel + ")"

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super(Client, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])
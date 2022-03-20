from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Season(models.Model):
    season=models.CharField(max_length=20)

    def __str__(self):
        return self.season

    class Meta:
        db_table='seasons'

class ForageType(models.Model):
    typename=models.CharField(max_length=20)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='foragetypes'

class Foraged(models.Model):
    name=models.CharField(max_length=250)
    foragetype=models.ForeignKey(ForageType, on_delete=models.DO_NOTHING)
    season=models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    datefound=models.DateField()
    amountfound=models.FloatField()
    location=models.CharField(max_length=250)
    comment=models.TextField(null=True, blank=True)
    dateentered=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def possiblePrice(self):
        self.price = self.amountfound * 15.50
        return self.price

    def __str__(self):
        return self.name

    class Meta:
        db_table='foraged'

class Foray(models.Model):
    name=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table='forays'

class Resource(models.Model):
    name=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    url=models.URLField()
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table='resources'
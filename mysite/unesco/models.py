from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=128)
    # iso = models.ForeignKey(Iso, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description = models.TextField(blank=True, null=True,)
    justification = models.TextField(blank=True, null=True,)
    longitude = models.FloatField(blank=True, null=True,)
    latitude = models.FloatField(blank=True, null=True,)
    area_hectares = models.FloatField(blank=True, null=True,)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name



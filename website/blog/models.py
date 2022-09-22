from django.db import models

class Place(models.Model):
    area=models.CharField(max_length=100)
    thumbnail=models.ImageField(upload_to="places", blank=True, null=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.area

class Character(models.Model):

    class Origin(models.TextChoices):
        SAYEN = 'Sayen'
        NAMEK = 'Namek'
        TERRIEN = 'Terrien'
        AUTRES = 'Autres'

    name=models.CharField(max_length=100)
    birth=models.IntegerField(default=0)
    origin=models.CharField(choices = Origin.choices, max_length=10)
    biography=models.TextField(blank=True)
    activity=models.CharField(max_length=100, blank=True)
    thumbnail=models.ImageField(upload_to="characters", blank=True, null=True)

    def __str__(self):
        return self.name

class Saga(models.Model):
    title=models.CharField(max_length=100)
    chap_start=models.IntegerField(default=0)
    chap_stop=models.IntegerField(default=1)
    resume=models.CharField(max_length=255, blank=True)
    biography=models.TextField(blank=True)
    thumbnail=models.ImageField(upload_to="sagas", blank=True, null=True)
    character=models.ForeignKey(Character, null=True, blank=True, on_delete=models.SET_NULL)
    place=models.ForeignKey(Place, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

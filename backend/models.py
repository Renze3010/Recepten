from django.db import models

# Create your models here.
class Opgeslagen(models.Model):
    UserPK = models.IntegerField()
    ReceptPK = models.IntegerField()

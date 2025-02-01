from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(validators=[MaxValueValidator(999),MinValueValidator(1)])
    address = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.id} - {self.name} - {self.email}"
    
    class Meta:
        ordering = ['id'] #Ascending
        #ordering = ['-id'] #Descending
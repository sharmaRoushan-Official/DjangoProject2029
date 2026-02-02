from django.db import models

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience = models.IntegerField()
    def __str__(self):
        return self.name 
    
# models.Model: Base class for all DB Models in Django ORM
# CharField: Text Data type
# IntegerField: Integer Data type [Number]
# __str__: Humain readable representation of the object
 

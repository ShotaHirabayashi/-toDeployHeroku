from django.db import models

# Create your models here.
class Address(models.Model):
    """Model definition for Address."""
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        """Unicode representation of Address."""
        return self.name

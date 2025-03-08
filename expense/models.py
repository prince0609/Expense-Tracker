from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
          id = models.AutoField(primary_key=True)
          user = models.ForeignKey(User, on_delete=models.CASCADE)
          amount = models.IntegerField(verbose_name='amount', null=True)
          description = models.TextField(null=True, blank=True)
          date = models.DateField(verbose_name='date', null=True)

          def __str__(self):
                  return self.description

class Profile(models.Model):
        id = models.AutoField(primary_key=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        budget = models.IntegerField(null=True, blank=True)
        month = models.IntegerField(null = True, blank=True)
        expense = models.IntegerField(null = True, blank=True)
        savings = models.IntegerField(null = True, blank=True)
        year = models.IntegerField(null=True, blank=True)


        def __str__(self):
                  return str(self.user.first_name)
          
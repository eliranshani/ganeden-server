from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=75)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
from django.db import models
from django.core.exceptions import ValidationError
import re

def validations(value_from_client):
    if all(x.isalpha() or x.isspace() for x in value_from_client):
        return 0
    else:
        raise ValidationError('Only letters, numbers and space are allowed')


class Todo_safe(models.Model):

    title = models.CharField(max_length = 225, validators = [validations])
    description = models.TextField(validators = [validations])

    def __str__(self) -> str:
        return self.title

class Todo_unsafe(models.Model):

    title = models.CharField(max_length = 225)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class user(models.Model):
    username = models.CharField(max_length = 225)
    password = models.CharField(max_length = 225)
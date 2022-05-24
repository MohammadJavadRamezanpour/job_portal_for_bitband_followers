from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_JOB_SEEKER = 'S'
    ROLE_EMPLOYER = 'E'
    ROLE_CHOICES = [
        (ROLE_JOB_SEEKER, 'Job seeker'),
        (ROLE_EMPLOYER, 'Employer')
    ]
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

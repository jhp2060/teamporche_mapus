from django.db import models
from account.models import University

class Campus(models.Model):
    university = models.OneToOneField(
        University,
        on_delete=models.CASCADE,
    )


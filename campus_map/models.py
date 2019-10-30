from django.db import models

class Campus(models.Model):
    university = models.OneToOneField(
        'account.University',
        on_delete=models.CASCADE,
    )


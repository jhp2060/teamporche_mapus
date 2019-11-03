from django.db import models

class Campus(models.Model):
    university = models.OneToOneField(
        'account.University',
        on_delete=models.CASCADE,
    )
    class Meta:
        verbose_name_plural="Campuses"
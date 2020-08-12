from django.db import models

# Create your models here.


class Stats(models.Model):
    name = models.CharField(max_length=200, null=False)
    request_date = models.DateTimeField(auto_now_add=True, blank=True)
    json_content = models.TextField(null=False)

    class Meta:
        unique_together = (('name', 'request_date'),)
        indexes = [
            models.Index(fields=['-request_date', ]),
        ]

from django.db import models

class block(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


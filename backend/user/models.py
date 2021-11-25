from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    api_id = models.CharField(max_length=100)
    api_hash = models.CharField(max_length=100)

    def _str_(self):
        return self.name

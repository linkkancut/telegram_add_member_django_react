from django.db import models


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    group_id = models.CharField(max_length=100)

    def _str_(self):
        return self.name

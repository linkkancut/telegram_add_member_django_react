from django.db import models


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=100)
    member_name = models.CharField(max_length=100)
    access_hash = models.CharField(max_length=100)

    def _str_(self):
        return self.name

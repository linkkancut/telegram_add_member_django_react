from django.db import models


class GroupMember(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=100)
    group_id = models.CharField(max_length=100)

    def _str_(self):
        return self.name

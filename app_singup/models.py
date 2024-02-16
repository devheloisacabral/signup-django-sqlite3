from django.db import models

class Users_table(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, blank=True, null=True)
    age = models.IntegerField()

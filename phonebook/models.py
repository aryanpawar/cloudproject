from django.db import models

class Contact(models.Model):
    c_name = models.CharField(max_length=30)
    c_no = models.IntegerField()

    def __str__(self):
        return self.c_name
    
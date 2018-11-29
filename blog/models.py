from django.db import models
from django.utils import timezone


class Item(models.Model):
    created_date = models.DateTimeField(
            default=timezone.now)
    trouble = models.BooleanField()
    oversea = models.BooleanField()
    status = models.CharField(max_length=50)
    operator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    company = models.CharField(max_length=200)
    customer = models.CharField(max_length=50)
    Tel = models.CharField(max_length=50)

    hard = models.CharField(max_length=200)
    soft = models.CharField(max_length=200)
    no_name = models.CharField(max_length=50)

    option = models.CharField(max_length=50)

    inquiry = models.TextField()
    answer = models.TextField()

    def Entry(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.hard + " : " + self.soft
from asyncio.base_futures import _PENDING
from django.db import models
from accounts.models import User

# Create your models here.

status = [
    ("pending", "PENDING"),
    ("processing", "PROCESSING"),
    ("processed", "PROCESSED")
]

deposit = [
    ("card", "CARD"),
    ("bank transfer", "BANK TRANSFER")
]

type = [
    ("deposit", "DEPOSIT"),
    ("withdraw", "WITHDRAWAL")
]

    
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=225, null=True, choices=type)
    amount = models.IntegerField()
    status = models.CharField(max_length=225, null=True, choices=status, default=_PENDING)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {} - {} - {}".format(self.user.first_name, self.type, self.status, self.date_created)
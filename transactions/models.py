# Django imports
from django.db import models

# App imports
from accounts.models import User


status = [
    ("pending", "PENDING"),
    ("processing", "PROCESSING"),
    ("processed", "PROCESSED")
]

type = [
    ("deposit", "DEPOSIT"),
    ("withdraw", "WITHDRAWAL")
]

    
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=225, null=True, choices=type)
    amount = models.IntegerField()
    status = models.CharField(max_length=225, null=True, choices=status, default="PENDING")
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "User: {} - Transaction Type: {} - Status: {} - Modified at: {}".format(self.user.first_name, self.transaction_type, self.status, self.date_created)

    class Meta:
        verbose_name_plural = "Transactions"
        db_table = "Transactions"
        indexes = [
            models.Index(fields=['user', 'transaction_type', 'status', 'date_created'])
        ]
    
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    available_amount = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Name: {} - Amount: {} - Created at: {} - Modified at: {}".format(self.user.first_name, self.available_amount, self.date_created, self.date_modified)

    class Meta:
        verbose_name_plural = "Wallets"
        db_table = "Wallets"
        indexes = [
            models.Index(fields=['user', 'available_amount', 'date_created', 'date_modified'])
        ]
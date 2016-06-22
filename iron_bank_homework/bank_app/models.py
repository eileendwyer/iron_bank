from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    DEBIT = 'DB'
    CREDIT = 'CR'

    TRANSACTION_CHOICES = ((DEBIT, 'DB'), (CREDIT, 'CR'))

    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_CHOICES, default=CREDIT)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=50)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.description

from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return f"{self.name} - {self.account_number}"


class LedgerEntry(models.Model):

    ENTRY_TYPES = (
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='ledger_entries'
    )

    transaction_id = models.CharField(max_length=100)

    entry_type = models.CharField(
        max_length=10,
        choices=ENTRY_TYPES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.account.name} - {self.entry_type} - {self.amount}"
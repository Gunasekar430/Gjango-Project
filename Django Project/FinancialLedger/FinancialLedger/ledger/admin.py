from django.contrib import admin
from .models import Account, LedgerEntry


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'account_number'
    )


@admin.register(LedgerEntry)
class LedgerEntryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'account',
        'transaction_id',
        'entry_type',
        'amount',
        'created_at'
    )
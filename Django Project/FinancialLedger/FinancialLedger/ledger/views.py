from decimal import Decimal
import uuid

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from .models import Account, LedgerEntry


def index(request):

    accounts = Account.objects.all()

    account_data = []

    for account in accounts:

        credit = LedgerEntry.objects.filter(
            account=account,
            entry_type='CREDIT'
        ).aggregate_total if False else None

        debit = Decimal('0')
        credit = Decimal('0')

        debit_entries = LedgerEntry.objects.filter(
            account=account,
            entry_type='DEBIT'
        )

        credit_entries = LedgerEntry.objects.filter(
            account=account,
            entry_type='CREDIT'
        )

        for entry in debit_entries:
            debit += entry.amount

        for entry in credit_entries:
            credit += entry.amount

        balance = credit - debit

        account_data.append({
            'account': account,
            'debit': debit,
            'credit': credit,
            'balance': balance
        })

    transactions = LedgerEntry.objects.select_related(
        'account'
    ).order_by('-created_at')

    return render(
        request,
        'ledger/index.html',
        {
            'account_data': account_data,
            'transactions': transactions
        }
    )


def create_account(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        account_number = request.POST.get('account_number')

        if not name or not account_number:
            messages.error(
                request,
                'All fields are required'
            )
            return redirect('index')

        if Account.objects.filter(
            account_number=account_number
        ).exists():

            messages.error(
                request,
                'Account number already exists'
            )
            return redirect('index')

        Account.objects.create(
            name=name,
            account_number=account_number
        )

        messages.success(
            request,
            'Account created successfully'
        )

        return redirect('index')

    return redirect('index')


@transaction.atomic
def transfer(request):

    if request.method == 'POST':

        from_account_id = request.POST.get(
            'from_account'
        )

        to_account_id = request.POST.get(
            'to_account'
        )

        amount = request.POST.get('amount')

        if not from_account_id or not to_account_id or not amount:
            messages.error(
                request,
                'All fields are required'
            )
            return redirect('transfer')

        try:
            amount = Decimal(amount)

        except:
            messages.error(
                request,
                'Invalid amount'
            )
            return redirect('transfer')

        if amount <= 0:
            messages.error(
                request,
                'Amount must be greater than 0'
            )
            return redirect('transfer')

        if from_account_id == to_account_id:
            messages.error(
                request,
                'Source and destination cannot be same'
            )
            return redirect('transfer')

        from_account = Account.objects.get(
            id=from_account_id
        )

        to_account = Account.objects.get(
            id=to_account_id
        )

        # Calculate source balance

        debit = Decimal('0')
        credit = Decimal('0')

        entries = LedgerEntry.objects.filter(
            account=from_account
        )

        for entry in entries:

            if entry.entry_type == 'DEBIT':
                debit += entry.amount

            elif entry.entry_type == 'CREDIT':
                credit += entry.amount

        balance = credit - debit

        # Check balance

        if balance < amount:

            messages.error(
                request,
                f'Insufficient balance. Available: ₹{balance}'
            )

            return redirect('transfer')

        # Generate transaction ID

        transaction_id = str(uuid.uuid4())

        # Debit source account

        LedgerEntry.objects.create(
            account=from_account,
            transaction_id=transaction_id,
            entry_type='DEBIT',
            amount=amount
        )

        # Credit destination account

        LedgerEntry.objects.create(
            account=to_account,
            transaction_id=transaction_id,
            entry_type='CREDIT',
            amount=amount
        )

        messages.success(
            request,
            f'₹{amount} transferred successfully'
        )

        return redirect('index')

    accounts = Account.objects.all()

    return render(
        request,
        'ledger/transfer.html',
        {
            'accounts': accounts
        }
    )
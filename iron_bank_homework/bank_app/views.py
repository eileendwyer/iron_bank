from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bank_app.models import Transaction
import datetime

class IndexView(TemplateView):
    template_name = "index.html"
    model = Transaction

class ProfileView(ListView):
    model = Transaction
    template_name = "profile_view"

    def account_balance(self):
        self.balance = 0
        transactions = Transaction.objects.filter(user=self.request.user)
        for transaction in transactions:
            print(transaction.transaction_type)
            if transaction.transaction_type == 'DB':
                if transaction.amount > self.balance:
                    raise ValidationError("Insufficient funds.")
                if self.balance >= transaction.amount:
                    self.balance -= transaction.amount
                elif transaction.transaction_type == 'CR':
                    self.balance += transaction.amount
        return self.balance

        def get_context_data(self):
            context = super().get_context_data
            balance = account_balance(self)
            context['balance'] = balance
            return context

class CreateNewUser(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = "profile_view.html"

    def get_queryset(self):
        return Transaction.objects.filter(id=self.request.user)

class CreateNewTransaction(CreateView):
    model = Transaction
    fields = ["amount", "transaction_type", "description"]

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        return super().form_valid(form)

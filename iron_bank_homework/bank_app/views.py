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
    template_name = "accounts/profile_view.html"

    def account_balance(self):
        balance = 0
        transactions = Transaction.objects.all()
        for transaction in transactions:
            if transaction.transaction_type == 'CR':
                balance += transaction.amount
            if transaction.transaction_type == 'DB':
                balance -= transaction.amount
        return balance

    def get_context_data(self):
        balance = self.account_balance()
        context = super().get_context_data()
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

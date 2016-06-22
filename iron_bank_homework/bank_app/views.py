from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bank_app.models import Transaction
import datetime

class IndexView(ListView):
    template_name = "index.html"
    model = Transaction

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).filter(created__lte=datetime.datetime.today(),
        created__gt=datetime.datetime.today()-datetime.timedelta(days=30))

    def get_context_data(self, **kwargs):
        context = super().get_context_data
        balance = 0
        transactions = Transaction.objects.filter(user=self.request.user)
        for transaction in transactions:
            print(transaction.transaction_type)
            if transaction.transaction_type == 'DB':
                if balance >= transaction.amount:
                    balance -= transaction.amount
            elif transaction.transaction_type == 'CR':
                balance += transaction.amount
        context['balance'] = balance
        return context

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = "transaction_detail_view.html"

    def get_queryset(self):
        return Transaction.objects.filter(id=self.request.user)

class CreateNewTransaction(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        return super().form_valid(form)

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
    template_name = "index.html"

class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class ProfileView(ListView):
    template_name = "accounts/profile.html"

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
                balance -= transaction.amount
            elif transaction.transaction_type == 'CR':
                balance += transaction.amount
        context['balance'] = balance
        return context

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = "transaction_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(TransactionDetailView, self).get_context_data(**kwargs)
        context['']

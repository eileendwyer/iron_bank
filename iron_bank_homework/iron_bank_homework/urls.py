"""iron_bank_homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bank_app.views import IndexView, CreateNewUser, AccountView, TransactionDetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url('^', include('django.contrib.auth.urls')),
    url(r'^create_new_user/$', CreateNewUser.as_view(), name="create_new_user"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^account_view/$', AccountView.as_view(), name="account_view"),
    url(r'^transaction/(?P<trans>/d+)/$', login_required(TransactionDetailView.as_view()),
    name="transaction_detail_view"),

]

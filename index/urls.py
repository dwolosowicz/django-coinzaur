from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from index.views import Home, UpdateExpense, Expenses
from index.views import CreateExpense

urlpatterns = [
    # Examples:
    # url(r'^$', 'coinzaur.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^expense/$', Expenses.as_view(), name='expense'),
    url(r'^expense/new$', CreateExpense.as_view(), name='expense_create'),
    url(r'^expense/(?P<object_id>\d+)/new$', UpdateExpense.as_view(), name='expense_update'),
]

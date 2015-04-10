from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from common.views import LoginRequiredMixin
from expenses.models import Expense
from index.forms import ExpenseForm


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index/base.html'


class Expenses(LoginRequiredMixin, ListView):
    template_name = 'index/expenses/list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.by_author(self.request.user)


class CreateExpense(LoginRequiredMixin, CreateView):
    template_name = 'index/expenses/form.html'
    form_class = ExpenseForm

    success_url = reverse_lazy('expense')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class UpdateExpense(LoginRequiredMixin, UpdateView):
    template_name = 'index/expenses/form.html'
    form_class = ExpenseForm

    success_url = '/'

    def get_object(self, queryset=None):
        return get_object_or_404(Expense, author=self.request.user, pk=self.request.GET['object_id'])

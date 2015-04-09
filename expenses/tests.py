from django.test import TestCase
from model_mommy import mommy
from common.tests import TimestampableTestCase, AuthorableTestCase
from expenses.models.expenses import Expense, Product


class ExpenseTestCase(AuthorableTestCase, TimestampableTestCase, TestCase):

    model = Expense

    def create_instance(self, **kwargs):
        return mommy.make(self.get_model(), **kwargs)

    def test_products_cost_with_no_products(self):
        """Expects the cost to be 0 if no products are specified"""

        expense = mommy.make(Expense)
        
        self.assertEqual(0, expense.products_cost())

    def test_products_cost_with_some_products(self):
        """Expects the cost to be equal to the sum of products costs"""

        expense = mommy.make(Expense)
        quantity = 5
        cost = 15

        mommy.make(Product, _quantity=quantity, cost=cost, expense=expense)

        self.assertEqual(quantity * cost, expense.products_cost())

    def test_not_specified_cost_without_products(self):
        """Expects the 'not specified' cost to be equal to total expense cost."""

        total_cost = 1000
        expense = mommy.make(Expense, total_cost=total_cost)

        self.assertEqual(expense.not_specified_cost(), total_cost)

    def test_not_specified_cost_with_products(self):
        """Expects the 'not specified' cost to be equal to total expense cost minus products_cost."""

        total_cost = 1000
        expense = mommy.make(Expense, total_cost=total_cost)

        product_cost = 100
        products_quantity = 5
        mommy.make(Product, _quantity=products_quantity, expense=expense, cost=product_cost)

        self.assertEqual(expense.not_specified_cost(), total_cost - product_cost * products_quantity)
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import unittest

from expenses import *

class Expenses_Test(unittest.TestCase):

    def setUp(self):
        """The setUp function runs before every test function."""

        #load expenses file
        self.expenses = import_expenses('expenses.txt')

    def test_import_expenses(self):

        #test existing total expenses
        self.assertAlmostEqual(45, self.expenses['clothes'])
        self.assertAlmostEqual(7.57, self.expenses['coffee'])
        self.assertAlmostEqual(135.62, self.expenses['entertainment'])

    def test_get_expense(self):

        #test getting expenses based on expense type
        self.assertAlmostEqual(7.57, get_expense(self.expenses, "coffee"))
        self.assertAlmostEqual(5, get_expense(self.expenses, "food"))

        # TODO insert 2 additional test cases
        #  Hint(s): Test non-existing expense types


    def test_add_expense(self):

        #test adding a new expense
        add_expense(self.expenses, "fios", 84.5)
        self.assertAlmostEqual(84.5, self.expenses.get("fios"))

        # TODO insert 2 additional test cases
        #  Hint(s): Test adding to existing expenses


    def test_deduct_expense(self):

        # test deducting from expense
        deduct_expense(self.expenses, "coffee", .99)
        self.assertAlmostEqual(6.58, self.expenses.get("coffee"))

        # test deducting from expense
        deduct_expense(self.expenses, "entertainment", 100)
        self.assertAlmostEqual(35.62, self.expenses.get("entertainment"))

        # TODO insert 2 additional test cases
        #  Hint(s):
        #   Test deducting too much from expense
        #   Test deducting from non-existing expense


    def test_update_expense(self):

        #test updating an expense
        update_expense(self.expenses, "clothes", 19.99)
        self.assertAlmostEqual(19.99, get_expense(self.expenses, "clothes"))

        # TODO insert 2 additional test cases
        #  Hint(s):
        #   Test updating an expense
        #   Test updating a non-existing expense


    def test_sort_expenses(self):

        #test sorting expenses by 'expense_type'
        expense_type_sorted_expenses = [('clothes', 45.0),
                                        ('coffee', 7.57),
                                        ('entertainment', 135.62),
                                        ('food', 5.0),
                                        ('rent', 825.0)]

        self.assertListEqual(expense_type_sorted_expenses, sort_expenses(self.expenses, "expense_type"))

        # TODO insert 1 additional test case
        #   Hint: Test sorting expenses by 'amount'


if __name__ == '__main__':
    unittest.main()

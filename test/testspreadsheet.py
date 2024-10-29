from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))
    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","1.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))
    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","'Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))
    def test_evaluate_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","'Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))
    def test_evaluate_simple_valid_formulas(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))
    def test_evaluate_simple_integer_formulas(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))
    def test_evaluate_simple_invalid_formulas(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","='Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))
    def test_simple_formula_with_references(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=B1")
        spreadsheet.set("B1", "42")
        self.assertEqual(42, spreadsheet.evaluate("A1"))





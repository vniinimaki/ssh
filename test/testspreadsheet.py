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
    def test_invalid_references(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=B1")
        spreadsheet.set("B1", "42.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))
    def test_circular_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=B1")
        spreadsheet.set("B1", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))
    def test_valid_arithmetic_formulas(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+3")
        self.assertEqual(4, spreadsheet.evaluate("A1"))
    def test_invalid_arithmetic_formulas(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+3.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))
    def test_division_by_zero_arithmetic_formulas(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1/0")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))
    def test_complex_arithmetic_formulas(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+3*2")
        self.assertEqual(7, spreadsheet.evaluate("A1"))
    def test_valid_arithmetic_formula_and_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+B1")
        spreadsheet.set("B1", "3")
        self.assertEqual(4, spreadsheet.evaluate("A1"))
    def test_invalid_arithmetic_formula_and_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+B1")
        spreadsheet.set("B1", "3.1")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))
    def test_circular_arithmetic_formula_and_reference(self):
        #We want to program to return #Circular if the formula contains a reference to a cell that refers back to the current cell
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","=1+B1")
        spreadsheet.set("B1", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))
    def test_formula_string_concatenation_valid(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","='Hello'&'World'")
        self.assertEqual("Hello World", spreadsheet.evaluate("A1"))


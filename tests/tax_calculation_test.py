import sys
import unittest
sys.path.append('../') 
from Models.tax_calculation import TaxCalculation

class TestTaxCalculation(unittest.TestCase,TaxCalculation):

    a_income = TaxCalculation(10000, 2000, 0.2, 0.05, 0.05, 500, 0.08, 94.65).a_income()

    def test_taxable_income(self):
       
        tax_calc = TaxCalculation(10000, 2000, 0.2, 0.05, 0.05, 500, 0.08, 94.65)  
        self.assertEqual(tax_calc.taxable_income(), 8905.35)

        tax_calc = TaxCalculation(10000, 2000, 0.2, 0.05, 0.05, 500, 0.08, 0)
        self.assertEqual(tax_calc.taxable_income(), 9000)

    def test_am_contribution(self):
        tax_calc = TaxCalculation(10000, 2000, 0.2, 0.05, 0.05, 500, 0.08, 94.65)
        self.assertEqual(tax_calc.am_contribution(), 712.43)

    def test_a_income(self):
        tax_calc = TaxCalculation( 10000, 2000, 0.2, 0.05, 0.05, 500, 0.08, 94.65)
        self.assertEqual(tax_calc.a_income(), 8192.92)

    def test_with_assert(self):
        assert self.a_income != 82192.92
        
    def test_type_of(self):
        assert type(self.a_income) == float


if __name__ == '__main__':
    unittest.main()
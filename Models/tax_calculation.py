from json import dumps

class TaxCalculation:
    def __init__(self,income,tax_deduction,tax_percent,pension_employee,pension_company,employee_benefits,am_contribution_percent,atp):
        self.income =  round(income, 2)
        self.tax_deduction = tax_deduction
        self.tax_percent = tax_percent
        self.pension_employee = pension_employee
        self.pension_company = pension_company
        self.employee_benefits = employee_benefits
        self.am_contribution_percent = am_contribution_percent
        self.atp = atp
    
    def taxable_income(self) :
        result = self.income-self.atp-(self.income*self.pension_employee)-self.employee_benefits
        return round(result, 2)
       
    def am_contribution(self): 
        result = self.taxable_income()*self.am_contribution_percent
        return round(result, 2)
        
    def a_income(self) :
        result = self.taxable_income()-self.am_contribution()
        return round(result, 2)
       
    def a_income_after_deduction(self):
        result = self.a_income()-self.tax_deduction
        return round(result, 2)
    
    def tax_of_income (self):
        result = self.a_income_after_deduction()*self.tax_percent
        return round(result, 2)
    
    def net_income(self):
        result = self.a_income() - self.tax_of_income()
        return round(result, 2)
    
    def gross_income(self):
        result = self.income*self.pension_company
        return round(result, 2)
    
    def result(self):
        return {
            "input": {
                "income": self.income,
                "tax_deduction": self.tax_deduction,
                "tax_percent": self.tax_percent,
                "pension_employee": self.pension_employee,
                "pension_company": round(self.pension_company - 1, 2),  # Corrected typo in variable name
                "employee_benefits": self.employee_benefits,
                "am_contribution_percent": self.am_contribution_percent,
                "atp": self.atp
            },
            "result": {
                "a_income": self.a_income(),
                "taxable_income": self.taxable_income(),
                "tax": self.tax_of_income(),
                "am_contribution": self.am_contribution(),
                "a_incomst_after_deduction": self.a_income_after_deduction(),              
                "income": {
                    "net_income": self.net_income(),
                    "gross_income": self.gross_income(),
                }
            }
        }

        
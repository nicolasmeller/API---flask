from flask import Flask, render_template
from Models.response_handler import Response
from Models.tax_calculation import TaxCalculation

app = Flask(__name__, template_folder='../templates')

def test():
   return render_template('index.html')

def jsontest(request):
    return Response(request).json(200),  

def taxcalc(request):
   
   income = float(request.args.get('income'))
   tax_deduction = float(request.args.get('tax_deduction'))
   tax_percent = float(request.args.get('tax_percent')) / 100
   pension_employee  = float(request.args.get('pension_employee')) / 100
   pension_company  = (float(request.args.get('pension_company')) / 100) + 1
   employee_benefits = float(request.args.get('employee_benefits'))
   am_contribution_percent = 0.08
   atp = 94.65
   
   tax_result = TaxCalculation(income,tax_deduction,tax_percent,pension_employee,pension_company,employee_benefits,am_contribution_percent,atp).result()
   return Response(tax_result).json() 
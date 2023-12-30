"""
simple Salary Calculator
"""

import sys


# maximum upper bounds of salary , and tax rate with and deduction amount in ETB
# tax rates in %, and dedcutions in ETB
# upperbounds in ETB
data = {
    1: {'salary': (0, 600),
    'TaxRate': 0,
    'Deduction': 0 },
    2: {'salary': (601, 1650),
    'TaxRate': 10,
    'Deduction': 60 },
    3: {'salary': (1651, 3200),
    'TaxRate': 15,
    'Deduction': 142.5 },
    4: {'salary': (3201, 5250),
    'TaxRate': 20,
    'Deduction': 302.50 },
    5: {'salary': (5251, 7800),
    'TaxRate': 25,
    'Deduction': 565 },
    6: {'salary': (7801, 10900),
    'TaxRate': 30,
    'Deduction': 955 },
    7: {'salary': (10901, None),
    'TaxRate': 35,
    'Deduction': 1500 },
}

print("\nEthiopian Government Tax Rates")
print("""
===================================================
No      Salary Range   TaxRate (%)  Deduction (ETB)
===================================================
1.      (0, 600)            0           0
2.      (601, 1650)         10          60 
3.      (1651, 3200)        15          142.5
4.      (3201, 5250)        20          302.50
6.      (5251, 7800)        25          565
6.      (7801, 10900)       30          955
7.      ( > 10,900)         35          1500
===================================================
""")


def get_rates(salary):
    # iterating over data
    taxRate = 0
    deduction = 0

    for key, value in data.items():
        # print(value.get('salary'))
        lower = value.get('salary')[0]
        upper = value.get('salary')[1]

        # print(lower, upper)
        if upper is None:
            taxRate, deduction  = (35, 1500)
        if upper is not None and (grossSalary >= lower and grossSalary <= upper):
            taxRate = value.get('TaxRate')
            deduction = value.get("Deduction")
            # print(taxRate, deduction)
            break
    return taxRate, deduction
   

if (len(sys.argv) < 3):
    print("Usage: netsalary <gross salary> <housing>")
    sys.exit()
else:
    grossSalary = float(sys.argv[1])
    housing = float(sys.argv[2])

def calculate_income():
    ## tax rates
    employeePensionRate = 0.07
    companyPensionRate = 0.11

    # employeePension = employeePensionRate * grossSalary

    otherTaxes = 0
    total_gross_salary = grossSalary + housing
    taxRate, deduction = get_rates(total_gross_salary)

    incomeTax = total_gross_salary * taxRate/100  - deduction
    employeePension = employeePensionRate * grossSalary
    # print(incomeTax, employeePension)
    # compute net income
    netIncome = total_gross_salary - incomeTax - employeePension - otherTaxes

    # printing toal net income
    print("-" * 50)
    print(f"\tYour Net Income is: {netIncome} Birr")
    print("\tThank You for using our Program")
    print("-" * 50)



# calling to calculate income
calculate_income()
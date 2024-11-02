import math
salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
print(salary_list)
last_salary= list(map(lambda i: i*0.3, salary_list))
result= list(map(lambda x, y: x+y,last_salary,salary_list ))
def simple_tax_calculator():
    global result
    return math.ceil(result)
print(result)
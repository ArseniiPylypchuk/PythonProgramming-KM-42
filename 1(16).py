import math


a_length= float(input("Довжина першої сторони"))
b_length= float(input("довєина другої сторони"))
c_length=float(input("Довжина третьої сторони"))

def check():
    if a_length <=0:
        raise ValueError
    if b_length <=0:
        raise ValueError
    if c_length <=0:
        raise ValueError
def deco(f):
    def triangle_ineq(i,j,k):
        if k >i+j:
            raise ValueError
        if i >k+j:
            raise ValueError
        if j >i+k:
            raise ValueError
        return f(i,j,k)
    return triangle_ineq

@deco
def area_calculation(a, b,c):
    piv_per= (a+b+c)/2
    geron = math.sqrt(piv_per*(piv_per-a)*(piv_per-b)*(piv_per-c))
    return geron

area = area_calculation(a_length, b_length, c_length)
print("Площа трикутника:" , area)
# This is method to add two number
import Calculator
#from mymath import Calculator
import math
from mymath import add,divide,substract
from mymath.multiple import multiple
from requests import addRequest, removeRequest

a = 1
b = 2
c = 3
d = 4
print(Calculator.add(3,4))
print(math.sqrt(2))
print(Calculator.add(a,b))
print(add.add(c,b))
print(divide.divide(d,b))
print(multiple.multiple(2,2))

ar = addRequest.AddRequest("r1","PKI")
print(ar.display())

dr = removeRequest.RemoveRequest("r2","yes")
print(dr.display())
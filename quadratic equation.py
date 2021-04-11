#standard form ax^2+bx+c....root the formula
import cmath #to perform sqroot() operation.
#coefficients of quadratic equation
a=1
b=5
c=6
#calculate discriminant
d=(b*b)-(4*a*c)
#finding the solutions
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)

print("The roots are:")
print(root1,root2)

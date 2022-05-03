import sympy
a = sympy.Symbol('a')
b = sympy.Symbol('b')
tenkai1 = sympy.expand((a + b)**2)
print(tenkai1)

x,y,z = sympy.symbols('x y z')
tenkai1 = sympy.expand((x+y+z)*(x**2+y**2+z**2-x*y-y*z-z*x))
print(tenkai1)

print(2**100)

print(float(2**100))
print(sympy.diff(x**3+5*x+2,x))
print(sympy.espand(x+1)**2)
print(sympy.apart(3/(x**-1)))
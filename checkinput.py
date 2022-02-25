from cmath import nan
import fractions
x = input()
try:
    res = int(x) #8
    print('Z')
except:
    pass
try:
    res = float(x) #8.1
    print('R')
except:
    pass
try:
    res = fractions.Fraction(x) #8/3 или 8e3
    print('Q')
except:
    pass
try:
    res = complex(x) #8+3j
    print('Q')
except:
    print(nan)  

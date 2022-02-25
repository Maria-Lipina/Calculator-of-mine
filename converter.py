from cmath import nan
from fractions import Fraction

def conversion(x):
    try: return int(x) #8
    except: pass
    try: return float(x) #8.1 или 1., 1.0, .1, 0.1, 1e+1, 1.e-3, 1.0e0
    except: pass
    try: return Fraction(x) #8/3
    except: pass
    try: return complex(x) #8+3j или 8-3j
    except: return nan

from fractions import Fraction

def conversion(x):
    try: return int(x)
    except: pass
    try: return float(x)
    except: pass
    try: return Fraction(x)
    except: pass
    try: return complex(x)
    except: return 'nan'

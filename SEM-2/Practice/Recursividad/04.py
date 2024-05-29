def expon(base, exponente):
    if exponente==0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * expon(base, exponente-1) 
print(expon(3,4))
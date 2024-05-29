def SumaNaturales(num):
    if num == 0:
        return False
    elif num == 1:
        return 1
    else:
        return num + SumaNaturales(num-1)
    
print(SumaNaturales(100))
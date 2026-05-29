def converter_temp (valor, origem="C"):
    if (origem == "C"):
        F = (valor - 32) * 5/9
        C = valor + 273.15
        return F, C
    elif (origem == "F"):
        c = (valor + 273.15)
        k = (c + 273.15)
        return c,k
    
c, k = converter_temp(100, origem="F")
print(c, k)

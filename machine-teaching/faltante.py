def faltante(numeros):
    i = int()
    while i<len(numeros):
        if (numeros[i])+1 != numeros[i+1]:
            return numeros[i] + 1
        i+= 1
    
print(faltante([1,2]))
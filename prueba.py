

def generarParentesis(n):
    solucion = []
    cadena = ""
    
    recursion(n,cadena,solucion)
    return solucion


def recursion(n,cad,sol):
    if(len(cad) == 2*n):
        sol.append(cad)
    else:
        izq=0
        der=0
        for i in range(len(cad)):
            if(cad[i] == '{'):
                izq = izq+1 
            if(cad[i] == '}'):
                der = der+1
        if(izq == der):
            recursion(n,cad+'{',sol)
        elif(der<izq):
            if(izq < n):
                recursion(n,cad+'{',sol)
            recursion(n,cad+'}',sol)

print(generarParentesis(5))


def imprimeNsubstring(cad,n):
    lista = []
    for i in range(len(cad)):
        for j in range(len(cad)+1):
            letra = cad[i:j]
            if(letra != ""):
                lista.append(letra)
        
    lista.sort()
    cadena = ""
    for substring in lista:
        cadena = cadena+substring
    return ' La cadena concatenada es: '+cadena+" y el caracter "+str(n)+" es:"+cadena[n-1]
            



print(imprimeNsubstring("dbac",3))


def superDigito(n,veces):
    n_str=""
    solucion=0
    for i in range(veces):
        n_str += str(n)
    return sumar(n_str)

def sumar(cadena):
    suma =0
    for numero in cadena:
        suma += int(numero)
    suma_str = str(suma)
    if(len(suma_str)>1):
        return sumar(suma_str)
    else:
        return int(suma)

    

print(superDigito(9875,1)) #resultado 2
print(superDigito(148,3)) #resultado 3
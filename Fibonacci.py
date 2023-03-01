n = 6
ultimo = 0
penul = 1
soma = 0
fibo = []
i =0

while i <= n:
    fibo.append(ultimo)
    print(fibo[i])
    soma = ultimo + penul
    
    ultimo = penul
    penul = soma
    i += 1
if(fibo[i-1] != n):
    print("esse numero não pertence a sequencia de fibonacci")
else:
    print("esse numero pertence a sequancia de fibonacci")
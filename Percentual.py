def percentagem(estado):
    return (100*estado)/soma

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
ou = 19849.53
estados = [sp,rj,mg,es,ou]
nomes = ["sp","rj","mg","es","ou"]

soma = sp+rj+mg+es+ou
i = 0
total = 0
while(i < len(estados)):
    print("percentagem de ",nomes[i],": ", percentagem(estados[i]),"%" )
    i+=1

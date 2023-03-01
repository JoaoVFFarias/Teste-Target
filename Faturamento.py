valores=[22174.1664,24537.6698,26139.6134,
         0.0,0.0,26742.6612,0.0,42889.2258,46251.174,11191.4722,
         0.0,0.0,3847.4823,373.7838,2659.7563,48924.2448,18419.2614,
         0.0,0.0,35240.1826,43829.1667,18235.6852,4355.0662,13327.1025,
         0.0,0.0,25681.8318,1718.1221,13220.495,8414.61
]
temp = [i for i in valores if i!=0]
temp.sort()
menor = temp[0]
temp.sort(reverse=True)
maior = temp[0]
print("O menor valor e: ",menor)
print("o maior valor e: ",maior)

dias = 0
media = sum(temp)/len(temp)
for i in temp:
    if (i>media):
        dias+=1
print("qtde de dias com faturamento maior que a media: ",dias)

# condições com IF e ELSE

nota1 = 7
nota2 = 8
nota3 = 5

media = (nota1 + nota2 + nota3) /3

if media >= 7:
    print("Aprovado - NOTA: " , round (media, 2))
elif media >= 5:
    print("Recuperação - NOTA: " , round (media , 2))
else: 
    print("Reprovado - NOTA: " , round (media , 2))       

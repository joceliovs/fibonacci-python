# esté progroma mostra uma sequencia finobocci em python

fino = int(input("Quantos termos: "))
# os primeiros 2 termos


n1,n2 = 0, 1
count = 0

# checagem se o numero é valido

if fino <= 0:
    print("Por favor Adcione um numero Positivo! " )

# se for apenas um termo, retornará 1

elif fino == 1:
    print(" Sequencia Finobocci ", fino)
    print(n1)

#gerador de sequencia
else:
    print("Sequencia Finobocci: ")
    while count < fino:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1

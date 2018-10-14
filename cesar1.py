abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nova_veta = []                      #list - můžu tam přidávat i odečítat


posun = int(input('O kolik chceš posunout šifru:'))
abeceda2 = abeceda[posun:] + abeceda[:posun]
veta = input('Napiš text:') 
veta = veta.upper()                 #všechny písmenka převede na velký písmena


for x in veta:
    index = abeceda2.index(x)       #zjištění pozice v abecedě2
    pismenko = abeceda[index]       #záměna písmenka z abecedy1
    nova_veta.append(pismenko)      #přidá nový písmenko do nového textu

nova_veta = "".join(nova_veta)      #spojí text dohromady

print(nova_veta)
    
    

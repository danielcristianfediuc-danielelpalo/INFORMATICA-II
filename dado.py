import random
n_lanza = 0
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0
buenos = [1,1,2,3,4,5,6]
lanzamiento = int(input("Introduce el número de lanzamientos"))
while lanzamiento > n_lanza:
    numero = random.choice(buenos)
    if numero == 1:
        n_lanza = n_lanza +1
        uno = uno +1
    elif numero == 2:
        n_lanza = n_lanza +1
        dos = dos +1
    elif numero == 3:
            n_lanza = n_lanza +1
            tres = tres +1
    elif numero == 4:
            n_lanza = n_lanza +1
            cuatro = cuatro +1
    elif numero == 5:
            n_lanza = n_lanza +1
            cinco = cinco +1
    elif numero == 6:
            n_lanza = n_lanza +1
            seis = seis +1
    else:
          break
print(f"Ha caído 1 {uno} veces, 2 {dos} veces, 3 {tres} veces, 4 {cuatro} veces, 5 {cinco} veces, 6 {seis} veces. En un total de {lanzamiento} tiros")
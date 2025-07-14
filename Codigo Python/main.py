vector = [3,1,3,4,3,3,3,3,-1]

t0 = 0              # Posicion inicial del vector
t1 = 4              # Para subir las posciones del vector
t2 = t0 + t1        # Segunda posicion del vector
t3 = -1             # Valor de parada
t4 = vector[t0]     # Primer valor del vector (Valor para comparar)
t5 = vector[t2]     # Valor a comprar
t6 = 0              # Contador
t7 = 1              # Incrementar contador

print(f"t0 = {t0}\nt1 = {t1}\nt2 = {t2}\nt3 = {t3}\nt4 = {t4}\nt5 = {t5}\nt6 = {t6}\n")

while t5 != t3:
    if t4 == t5:
        t6 += 1
    t2 += t1
    t5 = vector[t2]
    
print(f"El numero de veces que se repitio el primer valor es de: {t6}")

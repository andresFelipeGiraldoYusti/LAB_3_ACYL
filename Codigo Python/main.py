vector = [3,1,3,4,3,3,3,3,-1]

t0 = 0              # Posicion inicial del vector
t1 = 1              # Para subir las posciones del vector
t2 = t0 + t1        # Segunda posicion del vector
t3 = -1             # Valor de parada
t4 = vector[t0]     # Primer valor del vector (Valor para comparar)
t5 = vector[t2]     # Valor a comprar
t6 = 0              # Contador
t7 = 1              # Incrementar contador

while t5 != t3:
    if t4 == t5:
        t6 += 1
    t2 += t1
    t5 = vector[t2]
    
print("\n------------------------------------------------------------------------------------------------------------------")
print(f"\tEl numero de veces que se repitio el primer valor es de: {t6}")
print("------------------------------------------------------------------------------------------------------------------\n")
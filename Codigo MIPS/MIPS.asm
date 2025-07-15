.data
vector: .word 3, 1, 3, 3, 2, 3, 3, -1   # El -1 indica fin del vector
resultado: .word 0

.text
main:
    la $t0, vector        # $t0 = puntero al vector
    lw $t1, 0($t0)        # $t1 = primer elemento del vector (comparador)
    addi $t2, $zero, 0    # $t2 = contador de elementos iguales

recorrer:
    lw $t3, 0($t0)        # $t3 = vector[i]

    addi $t4, $zero, -1   # Valor centinela
    beq $t3, $t4, fin     # Si vector[i] == -1, termina

    bne $t3, $t1, siguiente
    addi $t2, $t2, 1      # Si son iguales, incrementar contador

siguiente:
    addi $t0, $t0, 4      # Mover al siguiente elemento
    j recorrer

fin:
    la $t5, resultado
    sw $t2, 0($t5)        # Guardar el resultado en memoria

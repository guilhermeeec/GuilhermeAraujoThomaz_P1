diferenca = 1
pi_anterior = -1
pi = 0
x = 1

while diferenca > 0.00000005:
    pi_anterior = pi
    if x%2 == 0:
        termo = (-4)/(2x-1)
    else:
        termo = (-4)/(2x-1)
    pi = pi + termo
    x += 1
    if pi > pi_anterior:
        diferenca = pi - pi_anterior
    else:
        diferenca = pi_anterior - pi

print(pi)


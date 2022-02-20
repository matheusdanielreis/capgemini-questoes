n = int(input())


contador = 1

while contador <= n:
    c = n-contador
    print(f'{c * " "}' f'{contador * "*" }')
    contador += 1


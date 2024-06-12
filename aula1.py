print("Olá")

def controlevelocidade():
    velocidade = 50
    contator = 0
    while contatortentativas < 10 and <= velocidade <= 100:
        print(f"velocidade atual: {velocidade} km")
        imput=("desejar aumentar (A) ou diminuir (D) a velocidade")
        if opcao == "A":
            velocidade += 10
        elif opcao == "D":
            velocidade -= 10
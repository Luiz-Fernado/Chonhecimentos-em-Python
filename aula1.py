def contadordevelocidade():
    velocidade = 50
    contador = 0
    print("chamou")
    while contador < 10 and velocidade >=0 and velocidade <= 100:
        print(f"velocidade atual= {velocidade} km")
        op = input("deseja aumentar (A) ou diminuir (D) a velocidade?").strip().upper()
        if op == "A":
            velocidade += 10
        elif op == "D":
             velocidade -= 10
        else:
            print("escolha invalida,tente novamente.")
            continue
        contador += 1

        if velocidade <= 0 or velocidade >= 100:
            break
        print(f"operacao finalizada,velocidade final: {velocidade} km")

contadordevelocidade()
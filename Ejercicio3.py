peso=int(input("Digite su peso: "))

altura=float(input("Digite su altura en metros: "))

calculo=peso/(altura*altura)

imc=round(calculo, 2)

print(f"Su IMC es de: {imc}")


#l ()

#cálculo do imc 
altura = float(input("Digite a altura em metros: "))
peso = float(input("Digite o peso em kg: "))
imc = peso / (altura ** 2)
print("O IMC para altura", altura, "m e peso", peso, "kg é:", imc)
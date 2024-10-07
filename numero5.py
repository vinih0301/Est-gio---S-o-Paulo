def inverter_palavra(s):
    resultado = ""
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

palavra = input("Digite uma palavra: ")
print(inverter_palavra(palavra))
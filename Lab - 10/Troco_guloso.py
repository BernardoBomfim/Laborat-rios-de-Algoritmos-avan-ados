def calcular_troco(valor_troco):

    moedas = [1.00, 0.50, 0.25, 0.10, 0.05]

    resultado = {}

    for moeda in moedas:
        if valor_troco >= moeda:
            quantidade_moedas = valor_troco // moeda
            valor_troco = round(valor_troco - quantidade_moedas * moeda, 2)  # Atualiza o valor do troco restante
            resultado[moeda] = int(quantidade_moedas)
    
    return resultado

valor_a_pagar = float(input("Digite o valor total do troco: R$ "))
troco = calcular_troco(valor_a_pagar)

print("\nMoedas necessárias para o troco:")
for moeda, quantidade in troco.items():
    print(f"Moeda de R${moeda:.2f}: {quantidade} unidade(s)")

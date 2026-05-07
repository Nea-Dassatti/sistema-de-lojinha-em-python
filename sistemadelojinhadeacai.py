#Boas Vindas!

print("Bem Vindo(a) à Casa de Açaí de Cleidinea Dassatti")


print("\n" + "-" * 50)
print("Cardápio")
print("-" * 50 + "\n")
print(f"{'TAMANHO':<10} {'Cupuaçu (CP)':<15} {'Açaí (AC)':<15}")
print("-" * 50)
print(f"{'P':<10} {'R$  9,00':<15} {'R$ 11,00':<15}")
print(f"{'M':<10} {'R$ 14,00':<15} {'R$ 16,00':<15}")
print(f"{'G':<10} {'R$ 18,00':<15} {'R$ 20,00':<15}")
print("-" * 50 + "\n")

# Inicializa o acumulador para somar os valores dos pedidos
valor_total = 0

# Estrutura de repetição principal 
while True:
    # Exigência de Código 2 de 8: Input do sabor com validação
    while True:
        sabor = input("Qual o sabor? (CP para Cupuaçu, AC para Açaí): ").upper()
        if sabor == "CP" or sabor == "AC":
            break  # Sai do loop se o sabor for válido
        else:
            print("Sabor inválido. Tente novamente.")

    

    # Input do tamanho com validação
    while True:
        tamanho = input("Qual o tamanho? (P/M/G): ").upper()
        if tamanho in ("P", "M", "G"):
            break  # Sai do loop se o tamanho for válido
        else:
            print("Tamanho inválido. Tente novamente.")

    # Pedido com tamanho inválido (simulado no loop acima)

    # Estrutura condicional aninhada para calcular o preço
    if sabor == "CP":
        if tamanho == "P":
            preco = 9
        elif tamanho == "M":
            preco = 14
        elif tamanho == "G":
            preco = 18
    elif sabor == "AC":
        if tamanho == "P":
            preco = 11
        elif tamanho == "M":
            preco = 16
        elif tamanho == "G":
            preco = 20

    # Adiciona o preço ao acumulador
    valor_total += preco

    # Pergunta se deseja pedir mais alguma coisa
    while True:
        mais_pedidos = input("Deseja pedir mais alguma coisa? (sim/nao): ").lower()
        if mais_pedidos == "sim":
            #continue (volta para o início do loop principal)
            break  # Sai do loop de pergunta para voltar ao início do pedido
        elif mais_pedidos == "nao":
            #break (sai do loop principal)
            break  # Sai do loop principal
        else:
            print("Resposta inválida. Por favor, responda 'sim' ou 'nao'.")

    if mais_pedidos == "nao":
        break  # Sai do loop principal se o usuário não quiser mais pedidos

# Exibindo o valor total
print(f'O valor total do seu pedido é: R$ {valor_total:.2f}')
print("Obrigada pela preferência!")
      



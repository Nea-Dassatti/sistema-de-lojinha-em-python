

# local de inserir dados
print('Bem Vindo(a) à loja de Cleidinea Dassatti!')
valor_unitário = float(input('Digite o valor unitário do produto: R$'))
quantidade_de_produtos = int(input('Digite a quantidade do produto: ')) 

#formula de desconto

valor_total_sem_desconto = valor_unitário * quantidade_de_produtos

#formulas de aplicação de descontos entre variaveis

if valor_total_sem_desconto < 2500:
    desconto = 0
elif valor_total_sem_desconto >= 2500 and valor_total_sem_desconto < 6000:
    desconto = 0.04 #4%
elif valor_total_sem_desconto >= 6000 and valor_total_sem_desconto < 10000:
    desconto = 0.07 #7%
else: 
    desconto = 0.11 #11%
    
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto)

#retorno dos resultados obtidos 

print(f'Resumo do Pedido:')
print(f'Valor Unitário: R$ {valor_unitário:.2f}')
print(f'Quantidade: {quantidade_de_produtos}')
print(f'Valor total sem desconto: R$ {valor_total_sem_desconto:.2f}')

if valor_total_sem_desconto >= 2500:
    print(f'Desconto aplicado:{desconto*100: .1f}%')
    print(f'Valor total com desconto:R${valor_total_com_desconto:.2f}')
else:
    print('Sem desconto aplicado')
print('Obrigada e Volte Sempre!') 


    

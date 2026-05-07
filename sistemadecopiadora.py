#Boas Vindas!

print('Bem Vindo(a) à Copiadora de Cleidinea Dassatti')


# Programa para sistema de cobrança de serviços de uma copiadora

def escolha_servico():
    # Função para selecionar o tipo de serviço e retornar seu custo por página

    while True:
        print("\nEntre com o serviço desejado:")
        print("DIG - Digitalização (R$1.10 por página)")
        print("ICO - Impressão Colorida (R$1.00 por página)")
        print("IPB - Impressão Preto e Branco (R$0.40 por página)")
        print("FOT - Fotocópia (R$0.20 por página)")
        
        servico = input("Digite a opção desejada (DIG/ICO/IPB/FOT): ").lower()
        
        # Mapeamento dos serviços e seus custos

        custos = {
            'dig': 1.10,
            'ico': 1.00,
            'ipb': 0.40,
            'fot': 0.20
        }
        
        if servico in custos:
            return custos[servico]
        else:
            print("Erro: Serviço inválido! Por favor, escolha DIG, ICO, IPB ou FOT.")

def num_pagina():
    # Função para obter número de páginas e calcular desconto

    while True:
        try:
            paginas = int(input("\nDigite o número de páginas: "))
            
            # Verifica se o número de páginas é válido

            if paginas >= 20000:
                print("Erro: Não aceitamos pedidos com 20000 ou mais páginas!")
                continue
                
            # Cálculo do desconto baseado no número de páginas

            if paginas < 20:
                desconto = 0
            elif 20 <= paginas < 200:
                desconto = 0.15
            elif 200 <= paginas < 2000:
                desconto = 0.20
            else:  # 2000 <= paginas < 20000
                desconto = 0.25
                
            # Retorna número de páginas após desconto

            paginas_com_desconto = paginas * (1 - desconto)
            return paginas_com_desconto, paginas, desconto
            
        except ValueError:
            print("Erro: Por favor, digite um número válido!")

def servico_extra():
    # Função para selecionar serviço adicional e retornar seu custo

    while True:
        print("\nDeseja algum serviço adicional?")
        print("0 - Nenhum (R$0.00)")
        print("1 - Encadernação Simples (R$15.00)")
        print("2 - Encadernação Capa Dura (R$40.00)")
        
        opcao = input("Digite a opção desejada (0/1/2): ")
        
        # Mapeamento dos serviços adicionais e seus custos

        extras = {
            '0': 0.00,
            '1': 15.00,
            '2': 40.00
        }
        
        if opcao in extras:
            return extras[opcao]
        else:
            print("Erro: Opção inválida! Por favor, escolha 0, 1 ou 2.")

# Programa principal
try:
    # Mensagem de boas-vindas

    print("Bem-vindo ao sistema de cobrança da copiadora!")
    
    # Obtém o serviço

    custo_pagina = escolha_servico()
    
    # Obtém número de páginas e desconto

    paginas_com_desconto, paginas_originais, desconto = num_pagina()
    
    # Obtém serviço extra

    custo_extra = servico_extra()
    
    # Cálculo do total

    total = (custo_pagina * paginas_com_desconto) + custo_extra
    
    # Exibe resumo do pedido
    
    print("\n=== Resumo do Pedido ===")
    print(f"Número de páginas original: {paginas_originais}")
    print(f"Desconto aplicado: {desconto*100:.0f}%")
    print(f"Número de páginas com desconto: {paginas_com_desconto:.2f}")
    print(f"Custo por página: R${custo_pagina:.2f}")
    print(f"Custo extra: R${custo_extra:.2f}")
    print(f"Total a pagar: R${total:.2f}")
    
except Exception as e:
    print(f"Erro no sistema: {str(e)}")
...


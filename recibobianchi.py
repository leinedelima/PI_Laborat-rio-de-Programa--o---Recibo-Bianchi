#Identificação do cliente.
NomeCliente = input("Digite o nome do cliente: ")

#Lista de produtos, com repetição de cadastro até que o usuário decida parar.
lista_produtos = []

while True:
    Produto = input("Digite o nome do produto: ")
    Quantidade = int(input("Digite a quantidade: "))
    ValorUni = float(input("Digite o valor unitário R$: "))
    Subtotal = float(Quantidade * ValorUni)

    lista_produtos.append({
        'produto': Produto,
        'quantidade': Quantidade,
        'valor_unitario': ValorUni,
        'subtotal': Subtotal
    })

    resposta = input("Deseja cadastrar outro produto? (s/n): ").strip().lower()
    if resposta != 's':
        break

#Solicitar ao usuário se deseja aplicar desconto.    
RespostaDesconto = input("Deseja aplicar desconto? (s/n): ").strip().lower()
if RespostaDesconto == 's':
    Desconto = float(input("Digite o valor do desconto R$: "))
else:
    Desconto = 0.0
    
#Solicitar ao usuário se a compra é parcelada.      
RespostaParcelado = input("A Compra é parcelada? (s/n): ").strip().lower()
if RespostaParcelado == 's':
    Parcelas = int(input("Digite o número de parcelas: "))
else:
    Parcelas = int(1)

#Solicitar ao usuário a forma de pagamento. Seguindo as opções, caso o usuário digite uma opção inválida, será solicitado novamente até que seja digitada uma opção válida.
OpcaoPagamento = 0

while not OpcaoPagamento in [1, 2, 3, 4]:
    print("Selecione a forma de pagamento: 1 - Crédito, 2 - Débito, 3 - Pix, 4 - Dinheiro")
    OpcaoPagamento = int(input("Digite a opção desejada: "))

if OpcaoPagamento == 1:
    FormaPagamento = "Crédito"
elif OpcaoPagamento == 2:
    FormaPagamento = "Débito"
elif OpcaoPagamento == 3:
    FormaPagamento = "Pix"
elif OpcaoPagamento == 4:
    FormaPagamento = "Dinheiro"
else:
    print("Opção inválida. Por favor, selecione uma opção válida. entre 1 e 4")

#Cálculo do total, total final e valor da parcela.    
Total = sum(lista_subtotal['subtotal'] for lista_subtotal in lista_produtos)
TotalFinal = Total - Desconto
ValorParcela = TotalFinal / Parcelas

#Exibição no formato para envio para o cliente.
print(f"*RECIBO CASA BIANCHI*")
print(f"```Cliente: {NomeCliente}")
print(f"Produtos Comprados: ")
for produto in lista_produtos:
    print(f"Item: {produto['produto']} | Quantidade: {produto['quantidade']} | Valor Unitário: R$ {produto['valor_unitario']:.2f} | Valor Total: R$ {produto['subtotal']:.2f}")
print(f"Desconto: R$ {Desconto:.2f}")
print(f"Forma de Pagamento: {FormaPagamento}")
print(f"Total dos Produtos: R$ {Total:.2f}")
print(f"Total com Desconto: R$ {TotalFinal:.2f}")
print(f"Parcelado em: {Parcelas} X")
print(f"Valor da Parcela: R$ {ValorParcela:.2f}```")
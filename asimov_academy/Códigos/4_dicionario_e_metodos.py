print('ASIMOV Academy\n \n')

#4.1 Dicionários
print('\n#4.1 Dicionários')
capitais = {
    'Brasil' : 'Brasília',
    'França' : 'Paris',
    'Japão' : 'Tóquio'
            }
for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')



#4.2 Operador in
print('\n#4.2 Operador in')
capitais = {
    'Brasil' : 'Brasília',
    'França' : 'Paris',
    'Japão' : 'Tóquio'
            }

pais = input('Informe o Pais para saber sua capital: ')

if pais in capitais:
    print(f'A capital de {pais} é {capitais[pais]}')
else: 
    print(f'Não há capital registratas para o país {pais}')
    


#4.3 Métodos | métodos de dicionários
print('\n#4.3 Métodos')
produtos = {
    'banana' : 3.60,
    'leite' : 4.90,
    'carne' : 15.50,
    'pão' : 9.00,
            }

produto = input('Informe o produto: ')

print(f'\nO preço do produto {produto} é {produtos.get(produto, 'Produto não disposível')}')

#setdefault: inserir valor
produtos.setdefault('milho', 3.90)

print('\nProdutos existentes:')
for par in produtos.items():
    print(par)






print('\n \n .....by Erick Saraiva')
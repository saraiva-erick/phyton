print('ASIMOV Academy\n \n')


#Variáveis
# print('Hello World')

# nome = input('Identificação\nSeu nome?')
# print('-'*10)
# print(f'Seu nome e {nome}')

#controle de FLuxo
# idade = int(input('Digite sua idade: '))
# if idade <18:
#     print(f'Você tem menos de 18 anos')
# elif idade == 18:
#     print(f'Você tem exatemante {idade} anos')
# else:
#     print('Você tem mais de 18 anos')

#3.sequencias e loops

##3.6for loop with range
print('\n \n##3.6for loop with range')
for n in range(10):
    print(f'O valor de n é: {n}')

print('\n \n##3.7 interando sobre sequancias')
##3.7 interando sobre sequancias
valores = [10, 20, 30, 3, -2, 17]
for valor in valores:
    print(f'O valor de n é: {valor}')


print('\n \n##3.7 interando sobre sequancias - lista/tupla')

clientes = [
    ('Erick', '4*.***.***.97', 'saraiva.erick@gmail.com'), 
    ('Luciana', '6*.***.***.74', 'clnm@gmail.com'),
    ('Beatriz', '8*.***.***.**', 'bia292000@gmail.com')
    ]

for cliente in clientes:
    #nome = cliente[0]
    #cpf = cliente[1]
    #email = cliente[2]
    nome, cpf, email = cliente 
    
    print(f'Cliente: {nome}\nCPF: {cpf}\neMail: {email}\n\n')


print('\n \n##3.8 while loops')
##3.8 while loops
n=0

while n < 3:
    print(f'O valor de n é: {n}')
    n +=1

print('Fim do wile loop')


print('\n \n##3.8 while loops')
##3.9 breake and continue
n=0

#while com break
while n <= 10:
    print(f'O valor de n é: {n}')
    n +=1
    if n == 5:
        break 
print('Fim do break loop')

#while com continue

for n in range (-5, 6):
    print(n)
    if n == 0:
        continue 
    resultado = 1 / n
    print(f'O resultado é: {resultado}')

print('Fim do continue loop')

#while True
while True:
    entrada = input('Digite qualquer coisa ("q") para sair): ')
    print(f'O valor digitado foi: {entrada}')
    if entrada == "q":
        break 
print('\nwhile true finalizado')




print('\n \n .....by Erick Saraiva')
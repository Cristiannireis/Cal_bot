

mensagem = ("Bem vindo ao Calbot. Vamos fazer umas contas?")
print(mensagem)
nome = input("Vamos nos conhecer. Qual o seu nome? ")
print(nome)

n1 = int(input("Digite um número "));
n2 = int(input("Digite outro número "));
opção = 0

while opção != 5:
    print("____"*20)
    print('''  Escolha uma opcção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] outros números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    print("____"*20)
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print("O resultado de {} x {} é {}".format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))
    elif opção == 4:
        print("Informe os números novamente")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor "))
    elif opção == 5:
        print("Finalizando ...")
    else:
        print("Opção inválida. Tente novamente")
print("Fim do programa! Volte sempre")


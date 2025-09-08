saida = ''

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão.'
    return a / b

def calculadora(num1, num2, operacao):
    if operacao.lower() == 'adicao' or operacao == '+':
        resultado = adicao(num1, num2)
    elif operacao.lower() == 'subtracao' or operacao == '-':
        resultado = subtracao(num1, num2)
    elif operacao.lower() == 'multiplicacao' or operacao == '*':
        resultado = multiplicacao(num1, num2)
    elif operacao.lower() == 'divisao' or operacao == '/':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida.'
    return resultado

while saida.lower() != 'n':
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação (Adicao, Subtracao, Multiplicacao, Divisao) ou (+, -, *, /): ')

    resultado = calculadora(numero1, numero2, operacao)

    print(f'O resultado da operação: {resultado}')

    saida = input('Deseja sair? (S/N): ')

print('Programa encerrado.')
#praticando try except e finally

try:

    nmr = int(input("Digite um numero para divisão: "))
    resultado = 5 / nmr
    print("o resultado é: ", resultado)
except ValueError as e:
    print("Você digitou um valor inválido")
    print (e)
except ZeroDivisionError as e:
    print("0 não é um número divisível", e)
except Exception as e:
    print("Impossível fazer o calculo, detalhes do erro: ", e)
finally:
    print("Processo finalizado.")
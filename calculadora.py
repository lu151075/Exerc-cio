executar = True
while executar :
    escolhas = '''
        [1] OU [+] para Somar
        [2] OU [-] para Subtração
        [3] OU [/] para Divisão
        [4] OU [*] para Multiplicação
        [5] para Sair
        '''
    
    print (escolhas)    
    operador =  input("Qual sua opção?: ")
    valor01  =  input("Qual o primeiro valor?: ")
    valor02  =  input("Qual o segundo valor?: ")
    valor01  =  int(valor01)
    valor02  =  int(valor02)

    texto_sair = '''
       [1]Não, desejo sair!
       [2]Sim, desejo realizar outro calculo

    '''
    # Soma
    if operador == "1"or operador == "+" or operador == "Somar" :
        resultado = valor01 + valor02
        print("Resultado da soma: " +  str(resultado))
        print(texto_sair)
        operador = input(" Deseja realizar outro calculo? ")
        if operador == "1" :
            executar = False


    # Subtração
    if operador == "2"or operador == "Subtração" or operador == "-" :
        resultado = valor01 - valor02
        print("Resultado da Subtração : " -  str(resultado))
        print(texto_sair)
        operador = input(" Deseja realizar outro calculo? ")
        if operador == "1" :
            executar = False
    

    # Divisão
    if operador == "3"or operador == " Divisão" or operador == "/" :
        resultado = valor01 / valor02
        print("Resultado da Divisão : " /  str(resultado))
        print(texto_sair)
        operador = input(" Deseja realizar outro calculo? ")
        if operador == "1" :
            executar = False


    # Multiplicação
    if operador == "4"or operador == "Multiplicação" or operador == "*" :
        resultado = valor01 * valor02
        print("Resultado da Multiplicação : " *  str(resultado))
        print(texto_sair)
        operador = input(" Deseja realizar outro calculo? ")
        if operador == "1" :
            executar = False




    # Sair
    
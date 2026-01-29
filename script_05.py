def calculadora():
    print("--- Calculadora Simples ---")
    print("Escolha a operaÃ§Ã£o digitando o nÃºmero referente:")
    print("1. Soma (+)")
    print("2. SubtraÃ§Ã£o (-)")
    print("3. MultiplicaÃ§Ã£o (*)")
    print("4. DivisÃ£o (/)")

    escolha = input("Digite o nÃºmero da operaÃ§Ã£o (1/2/3/4): ")

    # Verifica se a escolha Ã© vÃ¡lida
    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro nÃºmero: "))
            num2 = float(input("Digite o segundo nÃºmero: "))

            if escolha == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")

            elif escolha == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")

            elif escolha == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")

            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: NÃ£o Ã© possÃ­vel dividir por zero!")

        except ValueError:
            print("Erro: Por favor, digite apenas nÃºmeros.")
    else:
        print("OpÃ§Ã£o invÃ¡lida!")



calculadora()

# Usuário e senha fictícios para fins de estudo
Usuario = "admin"
Senha = "1133"

# Contador para controlar o número de tentativas
Tentativas = 0

# O programa permite no máximo 3 tentativas
while Tentativas < 3:

    # Solicita o nome de usuário
    Autenticacao = input("Qual é seu login? ")

    # Solicita a senha
    Autenticar = input("Qual é sua senha? ")

    # Aumenta o contador a cada tentativa
    Tentativas = Tentativas + 1

    # Verifica se o usuário e a senha estão corretos
    if Autenticacao == Usuario and Autenticar == Senha:

        # Login correto
        print("Acesso permitido")

        # Encerra o loop
        break

    else:

        # Login ou senha incorretos
        print("Acesso negado")

        # Verifica se o usuário já utilizou as 3 tentativas
        if Tentativas == 3:

            # Bloqueia o acesso após 3 erros
            print("Acesso bloqueado")

            # Encerra o loop
            break

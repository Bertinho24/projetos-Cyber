Usuario = "admin"
Senha = "1133"
Tentativas = 0

while Tentativas < 3:
    Autenticacao = input("Qual e seu login? ")
    Autenticar = input("Qual e sua senha? ")

    Tentativas = Tentativas + 1

    if Autenticacao == Usuario and Autenticar == Senha:
        print("Acesso permitido")
        break
    else:
        print("Acesso negado")

        if Tentativas == 3:
            print("Acesso bloqueado")
            break

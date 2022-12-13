import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_lenght = int(input("QUANTOS CARACTERES VOCE QUER EM SUA SENHA?>>> "))

    random.shuffle(characters)

    password  = []

    for x in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print("SUA SENHA É:", password)

option = input("VOCE QUER GERAR UMA SENHA? >>> (Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("OK, TCHAU!")
else: 
    print("OPÇÃO INVALIDA!")
    quit()
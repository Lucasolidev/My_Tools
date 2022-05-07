# Gerador de Senhas 2022
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Combinacao = lower_case + upper_case + number + symbols
Tamanho_pwd = 8

password = "".join(random.sample(Combinacao, Tamanho_pwd))

print("Gerador de Senhas 2022\n----------------------------\n")
print(f"Sua senha gerada foi: \n{password}\n")

import socket
import os


os.system('clear')


RED = "\033[91m"
NEON_PURPLE = "\033[95m"
RESET = "\033[0m"

# Logo e considerações com cores
print(f""" \n
{RED}

  ___  ___  ___  ___  _    ___  ___  ___ 
 | . \| . || . ||_ _|| |  | __>/ __>/ __>
 |   /| | || | | | | | |_ | _> \__ \\__ \
 |_\_\`___'`___' |_| |___||___><___/<___/
                                         

{RESET}
{NEON_PURPLE}
Autor: Rootless137
Aviso: Não sou responsável pelo mau uso desta ferramenta.
{RESET}

\n""")

print(logo)

ports = [22,21,20,443,445,80,8080,9009,9991,7070,3333,4040]

host = str(input("Insira o alvo: "))

for port in ports:
     

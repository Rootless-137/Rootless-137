import socket
import os


os.system('clear')


RED = "\033[91m"
NEON_PURPLE = "\033[95m"
RESET = "\033[0m"


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


ports = [22,21,20,443,445,80,8080,9009,9991,7070,3333,4040]

host = str(input("Insira o alvo: "))

for port in ports:
     socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     socket.settimeout(0.5)
     code = socket.connect_ex((host, port))
     if 0 in code:
         print(f"{port} \\\ open ")
     else:
          pass
     

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

r = 0
i = 0

host = str(input("Insira o alvo: "))

print(f"\n{RED} ! O SCAN ESTÁ EM ANDAMENTO ! {RESET}\n")


for port in ports:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.5)
     code = client.connect_ex((host, port))
     if code == 0:
         i = i + 1
         print(f" -> {port} || OPEN  ")
     else:
         r = r + 1
         print(f" -> {port} || CLOSED  ")
     
print(f"\n{NEON_PURPLE} O SCAN ENCONTROU {i} PORTAS ABERTAS e {r} FECHADAS {RESET}")

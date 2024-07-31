#!/usr/bin/env python3
import socket
import argparse
import os

os.system('clear')

# Cores para o terminal
RED = "\033[91m"
NEON_PURPLE = "\033[95m"
RESET = "\033[0m"

# Cabeçalho
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

parser = argparse.ArgumentParser(description='Ferramenta de escaneamento de portas.')
parser.add_argument('host', type=str, help='O endereço IP ou nome do host para escanear.')

args = parser.parse_args()
host = args.host

ports = [22,21,20,443,445,80,8080,9009,9991,7070,3333,4040]

# Contadores de portas abertas e fechadas
r = 0
i = 0

print(f"\n{RED} ! O SCAN ESTÁ EM ANDAMENTO ! {RESET}\n")

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    code = client.connect_ex((host, port))
    if code == 0:
        i += 1
        print(f" -> {port} ", "  || OPEN °")
    else:
        r += 1
        print(f" -> {port} ", "  || CLOSED •")
     
print(f"\n{NEON_PURPLE} O SCAN ENCONTROU {i} PORTAS ABERTAS e {r} FECHADAS {RESET}")
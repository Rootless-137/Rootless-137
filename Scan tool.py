#!/usr/bin/env python3
import socket
import argparse
import os
import re

# Limpa o terminal
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

# Função para validar o formato do endereço IP
def is_valid_ip(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if pattern.match(ip):
        return all(0 <= int(part) < 256 for part in ip.split('.'))
    return False

# Função para validar o formato do nome do host
def is_valid_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False

# Configuração dos argumentos de linha de comando
parser = argparse.ArgumentParser(description='Ferramenta de escaneamento de portas.')
parser.add_argument('host', type=str, help='O endereço IP ou nome do host para escanear.')

args = parser.parse_args()
host = args.host

# Verificação de validação de entrada
if not (is_valid_ip(host) or is_valid_host(host)):
    print(f"{RED}Erro: O endereço IP ou nome do host fornecido é inválido.{RESET}")
    exit(1)

# Lista de portas a serem escaneadas
ports = [22,21,20,443,445,80,8080,9009,9991,7070,3333,4040]

# Contadores de portas abertas e fechadas
r = 0
i = 0

print(f"\n{RED} ! O SCAN ESTÁ EM ANDAMENTO ! {RESET}\n")

# Escaneia as portas
for port in ports:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        code = client.connect_ex((host, port))
        if code == 0:
            i += 1
            print(f" -> {port} ", "  || OPEN °")
        else:
            r += 1
            print(f" -> {port} ", "  || CLOSED •")
        client.close()
    except socket.error as e:
        print(f"Erro de socket: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

print(f"\n{NEON_PURPLE} O SCAN ENCONTROU {i} PORTAS ABERTAS e {r} FECHADAS {RESET}")
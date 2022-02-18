import requests
from time import sleep
from colorama import Fore

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

print(Fore.RED + "   _____ ______ _______   ___   ___   ___     ____  _  __ ")
print(Fore.RED + "  / ____|  ____|__   __| |__ \ / _ \ / _ \   / __ \| |/ / ")
print(Fore.RED + " | |  __| |__     | |       ) | | | | | | | | |  | | ' /  ")
print(Fore.RED + " | | |_ |  __|    | |      / /| | | | | | | | |  | |  <   ")
print(Fore.RED + " | |__| | |____   | |     / /_| |_| | |_| | | |__| | . \  ")
print(Fore.RED + "  \_____|______|  |_|    |____|\___/ \___/   \____/|_|\_\ ")

print('')                  
                                                    
diretorios = input(Fore.GREEN + "Insira o nome do seu arquivo .txt: ")

with open(diretorios, "r") as file:   
                for diretorios in file.readlines():
        
                        diretorios_url = f"{diretorios.strip()}"
                        try:
                                response = requests.get(diretorios_url, headers=headers)

                                sleep(0.5)

                                if response.status_code==200:
                                        print(Fore.GREEN +f"[+] Diretório encontrado [+]: {diretorios_url}")
                                        arquivo = open('Resultados/encontrados.txt', 'a')
                                        arquivo.write(diretorios_url)
                                        arquivo.write('\n')
                                        arquivo.close
                                
                                if response.status_code==403:
                                        print(Fore.YELLOW +f"[+] Diretório com acesso proibido [+]: {diretorios_url}")
                                        arquivo = open('Resultados/acesso_proibido.txt', 'a')
                                        arquivo.write(diretorios_url)
                                        arquivo.write('\n')
                                        arquivo.close
                                
                                elif response.status_code!=200:
                                        print(Fore.RED +f"[+] Diretório não encontrado [+]: {diretorios_url}")
                                        arquivo = open('Resultados/nao_encontrados.txt', 'a')
                                        arquivo.write(diretorios_url)
                                        arquivo.write('\n')
                                        arquivo.close

                        except:
                                print(Fore.RED +f"[+] Diretório não encontrado [+]: {diretorios_url}")
                                arquivo = open('Resultados/nao_encontrados.txt', 'a')
                                arquivo.write(diretorios_url)
                                arquivo.write('\n')
                                arquivo.close
                                pass
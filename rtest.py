import requests
import urllib.request
import os
import random

valid_directs = []
valid_redirects = []
agents = {}

def req(file_name):
        try:
                r = requests.get(genc, headers=agents)
                os.mkdir(nome_empresa)
        except requests.exceptions.ConnectionError:
                print("\033[01;31mUrl inválida!!\033[0m")

        except FileExistsError:
                pass

        stats = r.status_code

        with open(f"{nome_empresa}/{file_name}", "a") as dit:
                if stats == 200 or stats == 304:
                        dit.write(f"{genc}\n")
                 
        if stats == 200:
                valid_directs.append(genc) 
                print(f"\033[01;32mPágina encontrada!! >>> {genc}\033[0m")
							  
        elif stats >= 300 and stats <= 399:
                valid_redirects.append(genc)
                print(f"\033[01;33mRedirecionamento de página >>> {genc}\033[0m")

        elif stats == 404:
                print(f"\033[01;31mPágina não encontrada!![X] => {genc}\033[0m")


def cookie():
        sec = requests.Session()
        try:
                r = sec.get(f"{ul}", headers=agents)
        except requests.exceptions.ConnectionError:
                print(f"\033[01;31mUrl Inválida!!\033[0m")
                exit(0)

        cookie = r.cookies.get_dict()
        if not os.path.exists(f"{nome_empresa}"):
                os.makedirs(nome_empresa)
                with open(f"{nome_empresa}/cookie.txt", "wb+") as ck:
                        for i in cookie:
                                ck.write(f"{i}: {cookie[i]}\n")

                        print(f"{i}: \033[01;32m{cookie[i]}\033[0m")

        elif os.path.exists:
                with open(f"{nome_empresa}/cookie.txt", "wb+") as ck:
                        for i in cookie:
                                ck.write(bytes(f"{i}: {cookie[i]}\n", encoding="utf-8"))

                        print(f"{i}: \033[01;32m{cookie[i]}\033[0m")


def html():
        html = urllib.request.urlopen(ul)
        fonte = html.read()
        if not os.path.exists(f"{nome_empresa}"):
                os.makedirs(nome_empresa)
                with open(f"{nome_empresa}/html.txt", "wb+") as html:
                        html.write(fonte)
                print("Código-fonte: \033[01;32m/html.txt\033[0m")

        elif os.path.exists:
                with open(f"{nome_empresa}/html.txt", "wb+") as html:
                        html.write(fonte)
                print("Código-fonte: \033[01;32m/html.txt\033[0m")

def header():
        r = requests.get(genc, headers=agents, allow_redirects=False)
        hd = r.headers
        if not os.path.exists(f"{nome_empresa}"):
                os.makedirs(nome_empresa)
                with open(f"{nome_empresa}/headers.txt", "wb+") as header:
                        for i in hd:
                                header.write(bytes(f"{i}: {hd[i]}\n", encoding="utf-8"))
                print("Header: \033[01;32m/headers.txt\033[0m")

        elif os.path.exists:
                with open(f"{nome_empresa}/headers.txt", "wb+") as header:
                        for i in hd:
                                header.write(bytes(f"{i}: {hd[i]}\n", encoding="utf-8"))
                print("Header: \033[01;32m/headers.txt\033[0m")



print("[1]https [2]http")
try:
        protocolo = int(input("==> "))
        if protocolo == 1:
                protocolo = "https://"
        elif protocolo == 2:
                protocolo = "http://"
        
        else:
                print("\033[01;31mErro na entrada de dados!!\033[0m")
                exit(0)

        url = str(input("Digite sua url >>> ")).lower()
except KeyboardInterrupt:
        print("\033[01;31mPrograma interrompido!\033[0m")


nome_empresa = str(input("Nome da empresa: ")).lower()
try:
        while True:
                with open("paginas.txt", "r") as leitura:
                        for i in leitura.readlines():
                                if i[0] == "/":
                                        ul = protocolo + url
                                        genc = protocolo + url + i
                                elif i[0] != "/":
                                        ul = protocolo + url 
                                        genc = protocolo + url + "/" + i

                                with open("user-agents.txt", "r") as agents_list:
                                        agt = list(agents_list)
                                        agt = random.choice(agt)
                                        agents["User-Agent"] = agt.rstrip("\n")
                                        req("diretorios.txt")
                                                     
                break

        html()
        cookie()
        header()
except KeyboardInterrupt:
        print("\033[01;31mPrograma interrompido!\033[0m")
        html()
        cookie()
        header()
        pass




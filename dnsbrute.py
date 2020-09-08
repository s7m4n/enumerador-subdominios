import sys
import dns.resolver
import pyfiglet

def banner():
    banner = pyfiglet.figlet_format('dnsbrute')
    print(banner)

def start():
    try:
        dominio = input('Digite o dominio sem http://:')
        arquivo = open('dominios.txt','r+')
        arqv = arquivo.read().splitlines()
        for subdominio in arqv:
            done = subdominio + '.' + dominio
            conexao = dns.resolver.query(done, 'a')
            print('Code 200 :', done, conexao)

    except Exception as error:
        print ("Error: " + str(error))
        pass

banner()
start()

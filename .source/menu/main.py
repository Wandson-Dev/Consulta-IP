from os import execl;from sys import argv, executable
from time import sleep
import time
import os
import random

def restart():                              
    execl(executable, executable, *argv)    
 
f = '\033[m';vermelho = '\033[31m';v = '\033[32m';amarelo = '\033[33m';azul = '\033[34m';roxo = '\033[35m';ciano = '\033[36m'
error = (f'  {vermelho}[ X ] ')

sucess = (f' {amarelo}[ ▪ ] ')

if __init__ = '__main__':
    exit()

from requests import get
from json import loads
time.sleep(3.2)
os.system("clear");time.sleep(1.5)

logoa = '.source/logo/logo.txt'
api_caminho ='.apis/'

with open(logoa, 'r') as file:
    conteudo = file.read()

print(f"{vermelho}{conteudo}");time.sleep(2.3);

menu = (f'''   {amarelo}

       {sucess} SEJA BEM VINDO AO MENU {sucess}


                ESCOLHA UMA FONTE DE CONSULTA
           {azul}[  {ciano}(1) {amarelo}IP API [recommended]{azul}] 
           {azul}[  {ciano}(2) {amarelo}IP TRACKER 100% [off] {azul}] 
           {azul}[  {ciano}(3) {amarelo}IP-WHOIS {azul}] 
           
           {azul}[  {ciano}(4) {amarelo}CONSULTAR MEU {ciano}IP {azul}] 
           
           
  {amarelo}×××××××××××××××××××××××××××××××××××××××××
              
           {azul}[  {ciano}(98) {amarelo} VERSÃO DO SCRIPT:{vermelho} null{azul}] 
           {azul}[  {ciano}(99) {amarelo}Verificar Atualizações{azul}] 
           
           {amarelo}By: Wandson Dev ||
           Instagram: @wandson.dev ||
           GitHub: Wandson-Dev ||

{azul} response {roxo}--> {ciano}''')

rss = input(menu)


if rss == '1':
   print(f'Certo, Aguarde Alguns Instantes...');time.sleep(1.2)
   try:
     os.system(f'python3 .sourcel/menu/ip-api.py')
   except:
     os.system(f'python3 .source/menu/ip-api.py')
   
   

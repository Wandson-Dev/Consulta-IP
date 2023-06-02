import base64
import atexit
import os


def remover_arquivo_temporario():
    if os.path.exists('temp.py'):
        os.remove('temp.py')


with open('index', 'r') as arquivo_codificado:
    conteudo_codificado = arquivo_codificado.read()


conteudo_texto = base64.b32decode(conteudo_codificado).decode('utf-8')


with open('temp.py', 'w') as arquivo_decodificado:
    arquivo_decodificado.write(conteudo_texto)


atexit.register(remover_arquivo_temporario)


exec(open('temp.py').read())
    
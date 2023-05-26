import base64
import atexit
import os

# Função para remover o arquivo temporário
def remover_arquivo_temporario():
    if os.path.exists('temp.py'):
        os.remove('temp.py')

# Lê o conteúdo do arquivo codificado
with open('index', 'r') as arquivo_codificado:
    conteudo_codificado = arquivo_codificado.read()

# Decodifica o conteúdo base32 para texto
conteudo_texto = base64.b32decode(conteudo_codificado).decode('utf-8')

# Salva o conteúdo decodificado em um novo arquivo temporário
with open('temp.py', 'w') as arquivo_decodificado:
    arquivo_decodificado.write(conteudo_texto)

# Registra a função de remoção do arquivo temporário
atexit.register(remover_arquivo_temporario)

# Executa o arquivo decodificado
exec(open('temp.py').read())
    
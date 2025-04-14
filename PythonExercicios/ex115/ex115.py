from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

opcao = 0
while True:
    titulo('MENU PRINCIPAL')
    menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    linha('MENU PRINCIPAL')
    opc = leiaInt('\033[32mSua Opção: \033[m')
    if opc == 1:
        lerArquivo(arq)
    elif opc == 2:
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        inserirPessoas(arq, nome, idade)
    elif opc == 3:
        break
    else:
        print('\033[31mERRO! Comando inválido! Tente novamente!\033[m')
linha('MENU PRINCIPAL')
print('Saindo do sistema... ', end='')
sleep(2)
print('Até logo!')
linha('MENU PRINCIPAL')
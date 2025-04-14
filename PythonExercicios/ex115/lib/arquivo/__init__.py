from ..interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()

def inserirPessoas(arq, nome='<desconhecido>', idade=0):
    titulo('CADASTRO')
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'Nome: {nome:-<25}Idade: {idade}\n')
        except:
            print('Houve um erro ao digitar no arquivo')
        else:
            print(f'Novo registro de {nome} cadastrado')
            a.close()



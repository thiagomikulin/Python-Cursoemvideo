import datetime
cadastro = {}
cadastro['nome'] = input('Digite o seu nome: ')
ano = int(input('Digite o ano do seu nascimento: '))
cadastro['idade'] = datetime.date.today().year - ano
cadastro['ctps'] = int(input('Digite o número da sua CTPS [se não tiver, digite 0]: '))
if cadastro['ctps'] != 0:
    cadastro['contrato'] = int(input('Digite o ano de contratação: '))
    cadastro['salario'] = float(input('Digite o seu salário: '))
    print(f'''O cadastrado {cadastro["nome"]} tem {cadastro["idade"]} anos de idade
O cadastrado tem CTPS de número {cadastro["ctps"]}''')
    if datetime.date.today().year - cadastro['contrato'] >= 35:
        print('Você já pode se aposentar!')
    else:
        print(f'Faltam {35 - (datetime.date.today().year - cadastro["contrato"])} anos para você poder se aposentar')
else:
    print(f'''O cadastrado {cadastro["nome"]} tem {cadastro["idade"]} anos de idade
O cadasstrado não possui carteira de trabalho''')
from pathlib import Path
from io import TextIOWrapper

def mostrarDic(d:dict):
    for chave, item in d.items():
        if chave != "TOTAL" and chave != 'TOTAL - #':
            print(f'{chave.title():<10} {"=":<3} {item:^12}')
        elif chave == "TOTAL":
            linhaFina()
            print(f'{chave:<10} {"=":<3} {item:^12}')
        else:
            print(f'{chave:<10} {"=":<3} {item:^12}')

def linhaTotal():
    print(f'{"="*30}TOTAL{"="*30}')

def linha():
    print('='*65)

def linhaFina():
    print('-'*65)

def juntar(b,x=False):
    junto = ''
    if not x:
        for arq in b:
            junto += f'{arq} | '
    if x:
        for arq in b:
            junto += f'\n\t\t{arq}'
    return junto

def criarDic(total=False):
    if not total:
        elementos = {'if':0, 'elif':0, 'else':0, 
                    'while':0, 'for':0, 
                    'try':0, 'except':0, 'finally':0,
                    'def':0, 'return':0,'pass':0,
                    'from':0, 'import':0,
                    'class':0, 'as':0,
                    'const':0,'#':0}
    else:
        elementos = {'if':0,'elif':0,'else':0,
                    'while':0,'for':0,
                    'try':0,'except':0,'finally':0,
                    'def':0,'return':0,'pass':0,
                    'from':0,'import':0,
                    'class':0,'as':0,
                    'const':0,'#':0, 
                    'TOTAL':0,'TOTAL - #':0}
    return elementos

def fila(arquivos:list, projeto, terminacao='.py'):
    for arquivopy in Path(projeto).glob(f'**/*{terminacao}'):              
        arquivos.append(arquivopy)
    return arquivos

def filaNome(nomes:list, projeto, terminacao='.py'):
    for arquivopy in Path(projeto).glob(f'**/*{terminacao}'):              
        nomes.append(arquivopy.name)
    return nomes

def logica(alvos:dict, arquivo:TextIOWrapper):
    aspasSimples = []
    aspasDuplas = []
    for linha in arquivo.readlines():
        for caractere in linha:
            if caractere == "'":
                aspasSimples.append(caractere)
            elif caractere == '"':
                aspasDuplas.append(caractere)
            
            if len(aspasSimples)%2 == 0 or len(aspasDuplas)%2 == 0:
                aspasSimples.clear()
                aspasDuplas.clear()

        for palavra in alvos.keys():
            if palavra in linha.replace(':','').split() and (len(aspasDuplas) == 0 and len(aspasSimples) == 0):
                if linha.find('#') == -1:
                    alvos[palavra] += linha.replace(':','').split().count(palavra)
                elif palavra == '#' and linha.find('#') != -1:
                    alvos[palavra] += linha.replace(':','').split().count(palavra)
                else:
                    if linha.find(palavra) < linha.find('#'):
                        alvos[palavra] += linha.replace(':','').split().count(palavra)
    return alvos

def somarAoTotal(inical:dict,total:dict):
    for chave, item in inical.items():
            total[chave] += item
            total['TOTAL'] += item
    total['TOTAL - #'] = total['TOTAL'] - total['#']
    return total


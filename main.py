from pathlib import Path
import func
import os

extensao = input("Selecione a linguagem a ser analisada: Python ou JS (py ou js)\n")
while extensao != "py" and extensao != "js":
    extensao = input('Digite apenas "py" ou "js": ')

func.linha()
print(f'Deseja analisar um projeto ou um unico arquivo? (1/2)')
func.linha()

x = int(input('Digite 1 ou 2 respectivamente. '))
while x != 1 and x != 2:
    x = int(input('Digite 1 ou 2 respectivamente. '))
    
if x == 1:
    print('Digite o caminho do projeto')
    print('Ex: D:\\Downloads\\python\\bot\\\n') 
    projeto = str(input('> ')) # adquire o caminho do projeto
    arquivos = []
    nomes = []
    erros = []
    try:
        arquivos = func.fila(arquivos, projeto, extensao) # cria a fila de arquivos a serem analisados
        nomes = func.filaNome(nomes, projeto, extensao)   # mesma coisa que o de cima, mas sem o caminho, so o nome do arquivo
    except Exception as e:
        print('[ERROR] Erro ao carregar projeto')
        exit()
    total = func.criarDic(total=True)
    for arquivo in arquivos:               # arquivos = lista de arquivos .py em um projeto
        func.linha()
        print(f'[+] {arquivo}')
        elementos = func.criarDic()

        try:
            abrirarquivo = open(f'{arquivo}', 'r', encoding='utf8')
            elementos = func.logica(elementos, abrirarquivo)
        except Exception:
            print(f'ALGUM ERRO OCORREU NO ARQUIVO "{arquivo}"\nPode haver algum caractere "ilegível" no arquivo.\n{Exception}')
            erros.append(arquivo)
        total = func.somarAoTotal(elementos, total)
        func.mostrarDic(elementos)
        abrirarquivo.close()

    if total['TOTAL'] > 0:
        func.linhaTotal()
        func.mostrarDic(total)
        nomes_todos = func.juntar(nomes)
        caminhos = func.juntar(arquivos,x=True)
        func.linhaFina()
        func.linha()
        print(f'Arquivos analisados: {nomes_todos}\nCaminhos analisados: {caminhos}')
        func.linha()
    else:
        print('Erro! Projeto nao encontrado ou extensao errada. Possivelmente há um erro de digitação no caminho dos arquivos.\nCaso esteja em alguma distro Linux, tente entrar na pasta e usar "." para se referir ao caminho dela.')
    if len(erros) > 0:
        print(f"ARQUIVO(S) COM ERRO: {str(erros).replace('WindowsPath(','').replace(')','')}")
        func.linha()


elif x == 2:
    print(f'Digite o caminho do arquivo (com {extensao}')
    print('Ex: D:\\Downloads\\python\\bot\\funcoes.py\n')
    arquivo = Path(str(input('> ')))
    try:
        abrirarquivo = open(f'{arquivo}', 'r', encoding='utf8')
    except Exception as e:
        print(f'[ERROR] Erro ao abrir arquivo.\n{e}')
        exit()
    elementos = func.logica(alvos=func.criarDic(), arquivo=abrirarquivo)
    abrirarquivo.close()
    func.linha()
    func.mostrarDic(elementos)
    
    total = func.criarDic(total=True)
    total = func.somarAoTotal(elementos,total)
    if total['TOTAL'] > 0:
        func.linhaFina()
        print(f'{"TOTAL":<10} {"=":<3} {total["TOTAL"]:^12}')
        print(f'{"TOTAL - #":<10} {"=":<3} {total["TOTAL - #"]:^12}')

    func.linha()
    print(f'Arquivo analisado: {arquivo.name}\nCaminho analisado: {arquivo}')
    func.linha()

from pathlib import Path
import func

extensao = input("Selecione a linguagem a ser analisada: Python ou JS (py ou js)\n")
while extensao != "py" and extensao != "js":
    extensao = input('Digite apenas "py" ou "js": ')

func.linha()
print(f'Deseja analisar um projeto ou um unico arquivo? \nExemplo:\n"D:\Downloads\python\\bot\\" para um projeto\n"D:\Downloads\python\\bot\\funcoes.py" para um arquivo unico')
func.linha()
x = int(input('Digite 1 ou 2 respectivamente. '))
if x == 1:
    arquivos = []
    nomes = []
    erros = []
    projeto = str(input("Digite o caminho do projeto: ")) # adquire o caminho do projeto

    total = func.criarDic(total=True)
    arquivos = func.fila(arquivos, projeto, extensao) # cria a fila de arquivos a serem analisados
    nomes = func.filaNome(nomes, projeto, extensao)   # mesma coisa que o de cima, mas sem o caminho, so o nome do arquivo
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
    arquivo = Path(str(input(f'Digite o caminho do arquivo (com {extensao}): ')))
    abrirarquivo = open(f'{arquivo}', 'r', encoding='utf8')
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

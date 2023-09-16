# Command Counter
Esse script lê projetos e arquivos em Python (ou em JS, mas com menos precisao) e retorna a quantidade de cada comando usado.
Os comandos serao filtrados e, caso estejam comentados (#) ou entre aspas ("" ou ''), nao serao contabilizados.

## Instalaçao e utilizaçao
### Requisitos
Python3 e [pip](https://pip.pypa.io/en/stable/)

### Linux 
```bash
git clone https://github.com/zecabum/Idenficador.git
```

```bash
cd Identificador
```

```bash
python3 main.py
```

### Windows
Baixe os arquivos [aqui](https://github.com/zecabum/Idenficador/archive/refs/heads/main.zip), extraia-os em alguma pasta e execute
```bash
python main.py
```

## Exemplo
    input:
    py
    2
    example.py
    
    output:
    If         =        4      
    Elif       =        1      
    Else       =        1      
    While      =        1      
    For        =        1      
    Try        =        1      
    Except     =        1      
    Finally    =        0      
    Def        =        0      
    Return     =        0      
    Pass       =        0      
    From       =        1      
    Import     =        2      
    Class      =        0      
    As         =        0      
    Const      =        0      
    #          =        4      
    -----------------------------------------------------------------
    TOTAL      =        17     
    TOTAL - #  =        13

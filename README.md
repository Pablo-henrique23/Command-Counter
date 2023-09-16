# Command Counter
Esse script lê projetos e arquivos em Python (ou em JS, mas com menos precisão) e retorna a quantidade de cada comando usado.
Os comandos serão filtrados e, caso estejam comentados (#) ou entre aspas ("" ou ''), não serão contabilizados.

## Instalação e utilização 
### Requisitos
Python3 e [pip](https://pip.pypa.io/en/stable/)

### Linux 
```bash
git clone https://github.com/zecabum/Command-Counter.git
```

```bash
cd Identificador/
```

```bash
python3 main.py
```

### Windows
Baixe os arquivos [aqui](https://github.com/zecabum/Command-Counter/archive/refs/heads/main.zip), extraia-os em alguma pasta e execute
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
    Continue   =        0
    From       =        1      
    Import     =        2      
    Class      =        0      
    As         =        0
    Lambda     =        0
    Const      =        0      
    #          =        4      
    -----------------------------------------------------------------
    TOTAL      =        17     
    TOTAL - #  =        13

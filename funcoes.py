def formatar(lista_termos:list) -> list:
    newList = []
    for palavra in lista_termos:
        if ',' in palavra:
            pre = palavra[:palavra.find(',')+1].replace(',','').strip()
            if '(' in palavra:
                pos = palavra[palavra.find(',')+1:palavra.find('(')]
            else:
                pos = palavra[palavra.find(',')+1:]
            palavra = f'{pos.strip()} {pre}'

        if ' ' in palavra:
            palavra = palavra.replace(palavra, fr'"{palavra}"')

        if '-' in palavra:
            newList.append(palavra.replace('-',''))
            newList.append(palavra.replace('-',' '))

        newList.append(palavra)

    return del_rep(newList)

def del_rep(lista:list) -> list:
    for palavra in lista:
        c = lista.count(palavra)
        if c>1:
            for x in range(0,c-1):
                lista.remove(palavra)
    return lista

def linha():
    print('-'*60)
    
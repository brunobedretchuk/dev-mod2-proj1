from operator import itemgetter

def centralizar(string:str):
    print(string.center(60 , '-'))

def listarTodos(lista):
    newLista = lista
    return newLista

def listarTransacoes(lista):
    newLista = lista
    return newLista

def listarComFiltro(lista , filtro):
    newLista = []
    for item in lista:
        if(item['_tipo'] == filtro):
            newLista.append(item)
    return newLista

def listarPorVendas(lista , filtro):
    lista_vendidos = []
    lista_disponiveis = []
    for item in lista:
        if(item['_cpf_comprador']):
            lista_vendidos.append(item)
        elif(not item['_cpf_comprador']):
            lista_disponiveis.append(item)
        
    if filtro == 'vendidos':
        return lista_vendidos
    elif filtro == 'disponiveis':
        return lista_disponiveis

def menuResponse(temp_lista_func , header):
    selecionarLista = int(input('\n1- Todos \n2 - Disponíveis \n3 - Vendidos \nOpção: '))  
    temp_lista = temp_lista_func
    if selecionarLista == 1:  
        auto_print(temp_lista , header)

    elif selecionarLista == 2:  
        lista = listarPorVendas(temp_lista , 'disponiveis')
        auto_print(lista , f'{header} Disponível')

    elif selecionarLista == 3:  
        lista = listarPorVendas(temp_lista , 'vendidos')
        auto_print(lista , f'{header} Vendido')

    
def maiorMenorVenda(lista , tipo):
    if tipo == 'maior':
        return max(lista , key=itemgetter('_valor'))
    elif tipo == 'menor':
        return min(lista , key=itemgetter('_valor'))


def auto_print(lista , header):
    for item in lista:
        centralizar(header)
        for atributo in item.items():
           
            print(f'{atributo[0]}: {atributo[1]}')
        centralizar('-')

def auto_print_item(item , header):
    centralizar(header)
    for atributo in item.items():
        print(f'{atributo[0]}: {atributo[1]}')
    centralizar('-')
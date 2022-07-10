import sys , os
import utils
from threading import Timer


from classes.veiculo import Veiculo
from classes.carro import Carro
from classes.moto_triciclo import MotoTricilo
from classes.camionete import Camionete

lista_veiculos = Veiculo._lista_veiculos
lista_transacoes = Veiculo._historico_transferencias

sys.path.append(os.path.join(sys.path[0],'classes'))

car1 = Carro.cadastrar_veiculo('20/10/2006' , 'Astra' , 'MHX-1234' , 12000 , 
'Verde' , 4 , 'Flex' , 250)
car2 = Carro.cadastrar_veiculo('12/01/2012' , 'Chevet' , 'MAB-9985' , 8000 , 
'Preto' , 2 , 'Gasolina' , 300)
car3 = Carro.cadastrar_veiculo('05/03/2010' , 'Corsel' , 'ADX-8555' , 5000 , 
'Verde' , 4 , 'Gasolina' , 500)

mot1 = MotoTricilo.cadastrar_veiculo('12/11/2012' , 'Hornet' , 'Abc-5533' , 3000 , 
'Vermelho' , 2 , 500)
tric1 = MotoTricilo.cadastrar_veiculo('10/10/2018' , 'CG' , 'UDL-4987' , 2000 , 
'Azul' , 3 , 125)

cam1 = Camionete.cadastrar_veiculo('18/05/2019' , 'Hilux' , 'MHC-3215' , 120000,
4 , 'Diesel' , 1500 , 1580)
cam2 = Camionete.cadastrar_veiculo('12/12/2020' , 'Frontier' , 'MCA-9875' , 13000,
4 , 'Gasolina' , 1250 , 2000)

car1.vender_veiculo('01234' , '29/04/2333')
tric1.vender_veiculo('0345613' , '10/10/2022')
cam1.vender_veiculo('654988' , '10/05/2022')



# execucao
utils.centralizar('DEVinCar')
while True:
    acao = int(input('\nSelecione uma das opções abaixo: \n1 - Lista de Veículos \n2 - Vendas\
    \nOpção: '))
    
    if acao == 1:
        selecionarClasse = int(input('Qual lista deseja visualizar?  \
        \n1- Todos \n2 - Carros \n3 - Motos/Triciclos \n4 - Camionetes \nOpção: '))

        if selecionarClasse == 1:
            utils.menuResponse(utils.listarTodos(lista_veiculos) , 'Veículo')
            
        elif selecionarClasse == 2:
            utils.menuResponse(utils.listarComFiltro(lista_veiculos , 'carro') , 'Carro')
     
        elif selecionarClasse == 3:
             utils.menuResponse(utils.listarComFiltro(lista_veiculos , 'moto_triciclo') , 'Moto/Triciclo')

        elif selecionarClasse == 4:
             utils.menuResponse(utils.listarComFiltro(lista_veiculos , 'camionete') , 'Camionete')
        else:
            break
        
        repeat = input('Deseja fazer mais alguma coisa? (s/n): ')
        if repeat != 's':
            break
    
    if acao == 2:
        selecionarClasse = int(input('Qual lista deseja visualizar?  \
        \n1- Transações \n2 - Maior venda \n3 - Menor venda \nOpção: '))

        if selecionarClasse == 1:
            lista = utils.listarTransacoes(lista_transacoes)
            utils.auto_print(lista , 'Transação')
            
        elif selecionarClasse == 2:
            item = utils.maiorMenorVenda(utils.listarPorVendas(lista_veiculos , 'vendidos') , 'maior')
            utils.auto_print_item(item , 'Maior Venda')
     
        elif selecionarClasse == 3:
            item = utils.maiorMenorVenda(utils.listarPorVendas(lista_veiculos , 'vendidos') , 'menor')
            utils.auto_print_item(item , 'Menor Venda')
             
        repeat = input('Deseja fazer mais alguma coisa? (s/n): ')
        if repeat != 's':
            break



















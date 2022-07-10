from multiprocessing.sharedctypes import Value
from classes.veiculo import Veiculo

class MotoTricilo(Veiculo):
    
    def __init__(self , data_fabricação:str , nome:str , placa:str , valor:float,
    cor:str, num_rodas:int , potencia:int):
        super().__init__(data_fabricação , nome , placa , valor, cor)
        self._num_rodas = num_rodas
        self._potencia = potencia 
        self._tipo = 'moto_triciclo'      
    
    def listar_informacoes(self):
        return f'Informações da moto/triciclo:\nNúmero do Chassi: {self._numero_chassi} \
            \nData de Fabricação: {self._data_fabricação} \nNome: {self._nome} \
            \nPlaca: {self._placa} \nValor: R${self._valor} \
            \nCpf do Comprador: {self._cpf_comprador} \nCor: {self._cor}\
            \Rodas: {self._num_portas} \nPotencia: {self._potencia}CV'


                
    @classmethod
    def cadastrar_veiculo(cls , data_fabricação , nome , placa , valor,
    cor , num_rodas , potencia):
        if num_rodas == 2 or num_rodas == 3:
            objeto = cls(data_fabricação , nome , placa , valor,
            cor, num_rodas , potencia)

            Veiculo._lista_veiculos.append(objeto.__dict__)
            return objeto
        
        else:
            raise ValueError('Desculpe, número de rodas deve ser 2 ou 3')



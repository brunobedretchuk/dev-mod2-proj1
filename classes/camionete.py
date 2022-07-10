from classes.veiculo import Veiculo

class Camionete(Veiculo):
    
    def __init__(self , data_fabricação:str , nome:str , placa:str , valor:float,
    num_portas:int , combustivel:str, potencia:int , capacidade:int):
        super().__init__(data_fabricação , nome , placa , valor , 'Roxo')
        self._num_portas = num_portas
        self._combustivel = combustivel
        self._potencia = potencia   
        self._capacidade = capacidade
        self._tipo = 'camionete' 
    
    def listar_informacoes(self):
        return f'Informações do carro:\nNúmero do Chassi: {self._numero_chassi} \
            \nData de Fabricação: {self._data_fabricação} \nNome: {self._nome} \
            \nPlaca: {self._placa} \nValor: R${self._valor} \
            \nCpf do Comprador: {self._cpf_comprador} \nCor: {self._cor}\
            \nPortas: {self._num_portas} \nCombustível: {self._combustivel}\
            \nPotência: {self._potencia} \nCapacidade: {self._capacidade} Litros'


                
    @classmethod
    def cadastrar_veiculo(cls , data_fabricação , nome , placa , valor,
    num_portas , combustivel , potencia , capacidade):
        if combustivel.lower() == 'diesel' or combustivel.lower() == 'gasolina':    
            objeto = cls(data_fabricação , nome , placa , valor,
            num_portas , combustivel , potencia , capacidade)

            Veiculo._lista_veiculos.append(objeto.__dict__)
            return objeto

        else:
            raise ValueError('Desculpe, combustível deve ser "Diesel" ou "Gasolina"')



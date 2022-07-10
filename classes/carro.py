from classes.veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self , data_fabricação:str , nome:str , placa:str , valor:float,
    cor:str, num_portas:int , combustivel:str, potencia:int):
        super().__init__(data_fabricação , nome , placa , valor, cor)
        self._num_portas = num_portas
        self._combustivel = combustivel
        self._potencia = potencia      
        self._tipo = 'carro' 
    
    def listar_informacoes(self):
        return f'Informações do carro:\nNúmero do Chassi: {self._numero_chassi} \
            \nData de Fabricação: {self._data_fabricação} \nNome: {self._nome} \
            \nPlaca: {self._placa} \nValor: R${self._valor} \
            \nCpf do Comprador: {self._cpf_comprador} \nCor: {self._cor}\
            \nPortas: {self._num_portas} \nCombustível: {self._combustivel}\
            \nPotencia: {self._potencia}'


                
    @classmethod
    def cadastrar_veiculo(cls , data_fabricação , nome , placa , valor,
    cor , num_portas , combustivel , potencia):
        if combustivel.lower() == 'flex' or combustivel.lower() == 'gasolina':
            objeto = cls(data_fabricação , nome , placa , valor,
            cor, num_portas , combustivel , potencia)

            Veiculo._lista_veiculos.append(objeto.__dict__)
            return objeto
        
        else:
             raise ValueError('Desculpe, combustível deve ser "Flex" ou "Gasolina"')




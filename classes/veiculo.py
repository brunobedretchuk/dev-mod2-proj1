import uuid

class Veiculo:
    _lista_veiculos = []
    _historico_transferencias = []

    def __init__(self , data_fabricação:str , nome:str , placa:str , valor:float, cor:str):
        self._numero_chassi = uuid.uuid4()
        self._data_fabricação = data_fabricação
        self._nome = nome
        self._placa = placa
        self._valor = valor
        self._cpf_comprador = None
        self._cor = cor


    def vender_veiculo(self , cpf_comprador , dataTransacao):
        if (not self._cpf_comprador):
            self._cpf_comprador = cpf_comprador
            self.dados_transacao(dataTransacao)
            Veiculo._historico_transferencias.append(self.dados_transacao(dataTransacao))
        else:
            print('Desculpe, este carro já foi vendido!')

    def dados_transacao(self , dataTransacao):
        transacao = {"dados": f'Número do Chassi: {self._numero_chassi}\
        \nData de Fabricação: {self._data_fabricação} \nNome: {self._nome}' ,
            "cpf_comprador" : self._cpf_comprador , "valor" : self._valor ,
            "data" : dataTransacao}

        return transacao
   
    def listar_informacoes(self):
        return f'Informações do veículo:\nNúmero do Chassi: {self._numero_chassi} \
            \nData de Fabricação: {self._data_fabricação} \nNome: {self._nome} \
            \nPlaca: {self._placa} \nValor: R${self._valor} \
            \nCpf do Comprador: {self._cpf_comprador} \nCor: {self._cor}'


    def alterar_informacoes(self , cor = None , valor = None):
        if (cor):
            self._cor = cor
        if(valor):
            self._valor = valor

        print('Informações do veículo alteradas com sucesso \n')
        print(self.listar_informacoes)

                
    @classmethod
    def cadastrar_veiculo(cls , data_fabricação , nome , placa , valor,
    cor):
        objeto = {"data_fabricacao" : data_fabricação , "nome" : nome ,
        "placa" : placa ,"valor" : valor , "cor" : cor , "CPF Comprador":None}
        Veiculo._lista_veiculos.append(objeto)
        return cls(data_fabricação , nome , placa , valor,
        cor)




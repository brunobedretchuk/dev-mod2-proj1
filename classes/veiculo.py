import uuid

class Veiculo:
    lista_veiculos = []

    def __init__(self , data_fabricação:str , nome:str , placa:str , valor:float,
    cpf_comprador:str , cor:str):
        self._numero_chassi = uuid.uuid4()
        self._data_fabricação = data_fabricação
        self._celular = celular
        self._email = email
        self._enderecos = []

    def exibir_pessoa(self):
        return (f'A pessoa cadastrada é:\nnome: {self._nome} \
            \ncelular: {self._celular} \nemail: {self._email} \
            \n{self.lista_enderecos()}')    
   
    def insere_endereco(self , logradouro , numero , complemento , bairro,
    cidade , uf):
        self._enderecos.append(Endereco.cadastrar_endereco(logradouro , numero , complemento , bairro,
    cidade , uf))

    def lista_enderecos(self):
        for endereco in self._enderecos:
            dict = {'logradouro': endereco.logradouro , 'numero': endereco.numero ,
            'complemento': endereco.complemento , 'bairro': endereco.bairro ,
            'cidade': endereco.cidade , 'uf': endereco.uf ,}
            str = f'Endereço {self._enderecos.index(endereco) + 1}:'
            
            for item in dict.items():
                str  += indent(f'\n{    item[0]}: {item[1]}' , 4)
        return str
                
    @classmethod
    def cadastrar_pessoa(cls , nome , celular , email):
        return cls(nome , celular , email)

    @property
    def enderecos(self):
        return self._enderecos


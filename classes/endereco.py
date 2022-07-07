import json
import os

class Endereco:
    def __init__(self , logradouro:str , numero:int , complemento:str,
                bairro:str , cidade:str , uf:str):
        self.__logradouro = logradouro
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__uf = uf

    def exibir_endereco(self):
        return (f'O endereço cadastrado é:\nlogradouro: {self.__logradouro} \
            \nnumero: {self.__numero} \ncomplemento: {self.__complemento} \
            \nbairro: {self.__bairro} \ncidade: {self.__cidade} \
            \nuf: {self.__uf}')
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__ , sort_keys=True , indent=4)

    def salvar_endereco(self):
        with open(os.path.join('C:/Users/Bruno V/Documents/GitHub/m2s5/data' , self.__logradouro) , 'w') as f:
            json.dump(self.toJSON() , f)

    @classmethod
    def cadastrar_endereco(cls , logradouro , numero , complemento , bairro,
    cidade , uf):
        return cls(logradouro , numero , complemento , bairro,
    cidade , uf)

    @property
    def logradouro(self):
        return self.__logradouro
    @property
    def numero(self):
        return self.__numero
    @property
    def complemento(self):
        return self.__complemento
    @property
    def bairro(self):
        return self.__bairro
    @property
    def cidade(self):
        return self.__cidade
    @property
    def uf(self):
        return self.__uf
    

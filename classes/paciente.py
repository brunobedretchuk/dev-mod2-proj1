# import json , os , textwrap
# from classes.pessoa import Pessoa

# class Paciente(Pessoa):
#     def __init__(self , nome:str , celular:int , email:str,
#     rg:int , cpf:str , telefone:int , convenio:str ,
#     data_de_nascimento:str):
#         super().__init__(nome , celular , email)
#         self.__rg = rg
#         self.__cpf = cpf
#         self.__telefone = telefone
#         self.__convenio = convenio
#         self.__data_de_nascimento = data_de_nascimento
        

#     def exibir_paciente(self):
#         return (f'O paciente cadastrado é:\nnome: {self._nome} \
#             \ncelular: {self._celular} \nemail: {self._email} \
#             \nrg: {self.__rg} \ncpf: {self.__cpf} \
#             \ntelefone: {self.__telefone} \nconvenio: {self.__convenio} \
#             \ndata_de_nascimento: {self.__data_de_nascimento}\
#             \n{self.lista_enderecos()}')
    
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__ , sort_keys=True , indent=4)

#     def salvar_paciente(self):
#         with open(os.path.join('C:/Users/Bruno V/Documents/GitHub/m2s5/data' , self.__nome) , 'w') as f:
#             json.dump(self.toJSON() , f)


                
#     @classmethod
#     def cadastrar_paciente(cls , nome , celular , email , rg , cpf , telefone , convenio ,
#     data_de_nascimento):
#         return cls(nome , celular , email , rg , cpf , telefone , convenio ,
#     data_de_nascimento)

#     @property
#     def enderecos(self):
#         return self.__enderecos


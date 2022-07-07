# import json , os , textwrap
# from classes.pessoa import Pessoa

# class Medico(Pessoa):
#     def __init__(self , nome:str , celular:int , email:str,
#     crm:int , telefone_secundario:int):
#         super().__init__(nome , celular , email)
#         self.__crm = crm
#         self.__telefone_secundario = telefone_secundario        

#     def exibir_medico(self):
#         return (f'O médico cadastrado é:\nnome: {self._nome} \
#             \ncelular: {self._celular} \nemail: {self._email} \
#             \crm: {self.__crm} \ntelefone secundário: {self.__telefone_secundario} \
#             \n{self.lista_enderecos()}')
    
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__ , sort_keys=True , indent=4)

#     def salvar_medico(self):
#         with open(os.path.join('C:/Users/Bruno V/Documents/GitHub/m2s5/data' , self.__nome) , 'w') as f:
#             json.dump(self.toJSON() , f)


                
#     @classmethod
#     def cadastrar_medico(cls , nome , celular , email , crm , telefone_secundario):
#         return cls(nome , celular , email , crm , telefone_secundario)

#     @property
#     def enderecos(self):
#         return self.__enderecos


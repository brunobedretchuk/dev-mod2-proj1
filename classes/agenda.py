# import json
# import os

# class Agenda:
#     def __init__(self , crm_medico:int , cpf_paciente:str , dia:int,
#                 mes:int , ano:int , hora:str , observacao:str):
#         self.__crm_medico = crm_medico
#         self.__cpf_paciente = cpf_paciente
#         self.__dia = dia
#         self.__mes = mes
#         self.__ano = ano
#         self.__hora = hora
#         self.__observacao = observacao

#     def exibir_agenda(self):
#         return (f'Horário na Agenda:\nMédico CRM: {self.__crm_medico} \
#             \nPaciente CPF: {self.__cpf_paciente} \ndia: {self.__dia} \
#             \nmês: {self.__mes} \nano: {self.__ano} \
#             \nhorário: {self.__hora} \nobservacao: {self.__observacao}'')
    
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__ , sort_keys=True , indent=4)

#     def salvar_agenda(self):
#         with open(os.path.join('C:/Users/Bruno V/Documents/GitHub/m2s5/data' , self.__dia +'_'+self.__mes+'_'+self.__ano) , 'w') as f:
#             json.dump(self.toJSON() , f)

#     @classmethod
#     def cadastrar_agenda(cls , crm_medico , cpf_paciente , dia , mes,
#     ano , hora , observacao):
#         return cls(crm_medico , cpf_paciente , dia , mes,
#     ano , hora , observacao)

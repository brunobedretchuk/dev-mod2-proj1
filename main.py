import sys , os

from classes.endereco import Endereco
# from classes.pessoa import Pessoa
# from classes.paciente import Paciente
# from classes.medico import Medico
# from classes.agenda import Agenda

sys.path.append(os.path.join(sys.path[0],'classes'))




end1 = Endereco.cadastrar_endereco('rua Almirante' , 120 , 'bloco B' , 'floresta' , 
'São José' , 'SC')

print(end1.exibir_endereco())











# paciente1 = Paciente.cadastrar_paciente('Bruno' , 48991804224 , 'brunobedretchuk@gmail.com',
# '4.444-444' , '091.999.652-87' , 1321321 , 'unimed' , '29/04/1996')
# paciente1.insere_endereco('rua Almirante' , 120 , 'bloco B' , 'floresta' ,
# 'São José' , 'SC')

# med1 = Medico.cadastrar_medico('Zico' , 48991804224 , 'xxxxxxx@gmail.com',
# '12345' , 48991804224)
# med1.insere_endereco('rua Xico' , 120 , 'bloco B' , 'floresta' ,
# 'São José' , 'SC')

# print(paciente1.exibir_paciente())
# print(med1.exibir_medico())

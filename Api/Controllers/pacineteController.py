    

from Paciente import Paciente



def Cadastrar():
    pNome = input("nome: ")
    pIdade = int(input("idade: "))
    pPeso = input("peso: ")
    paltura = input("altura: ")
    
    testePaciente = Paciente(pNome, pIdade, pPeso, paltura)

    print(testePaciente.getJson())


Cadastrar()
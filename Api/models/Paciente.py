class Paciente():
    nome: str
    idade: int
    peso: int
    altura: int

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

class Remedio():
    nome: str 
    quantidade: int
    isComprimido: bool

    def __init__(self, nome, quantidade, isComprimido):
        self.nome = nome
        self.quantidade = quantidade
        self.isComprimido = isComprimido
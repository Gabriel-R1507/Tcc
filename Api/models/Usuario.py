class Usuario():
    login: str
    senha: str
    idPaciente: int
    isAdmin: bool

    def __init__(self, login, senha, idPaciente, isAdmin):
        self.login = login
        self.senha = senha
        self.idPaciente = idPaciente
        self.isAdmin = isAdmin
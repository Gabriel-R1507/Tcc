import datetime

class Vinculo():
    paciente: int
    remedio: int
    data: datetime
    isLow: bool

    def __init__(self, paciente, remedio, data, isLow):
        self.paciente = paciente
        self.remedio = remedio
        self.data = data
        self.isLow = isLow

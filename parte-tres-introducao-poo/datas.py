class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def forma_data(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
import pandas as pd
from datetime import datetime

class ManutencaoManager:
    def __init__(self):
        self.manutencoes = []

    def registrar_manutencao(self, placa, descricao, km_realizado):
        self.manutencoes.append({
            "Placa": placa,
            "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Descrição": descricao,
            "KM Realizado": km_realizado
        })

    def gerar_relatorio(self):
        df = pd.DataFrame(self.manutencoes)
        df.to_csv("data/manutencoes.csv", index=False)
        print("Relatório de manutenções salvo em data/manutencoes.csv")

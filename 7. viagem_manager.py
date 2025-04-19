import pandas as pd
from datetime import datetime

class ViagemManager:
    def __init__(self):
        self.viagens = []

    def registrar_viagem(self, placa, origem, destino, km, combustivel):
        self.viagens.append({
            "Placa": placa,
            "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Origem": origem,
            "Destino": destino,
            "Km": km,
            "Combustível (L)": combustivel
        })

    def gerar_relatorio(self):
        df = pd.DataFrame(self.viagens)
        df.to_csv("data/viagens.csv", index=False)
        print("Relatório de viagens salvo em data/viagens.csv")

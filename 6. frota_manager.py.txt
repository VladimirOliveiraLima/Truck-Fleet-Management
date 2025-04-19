import pandas as pd

class FrotaManager:
    def __init__(self):
        self.caminhoes = []

    def cadastrar_caminhao(self, placa, modelo, ano):
        self.caminhoes.append({
            "Placa": placa,
            "Modelo": modelo,
            "Ano": ano
        })

    def gerar_relatorio(self):
        df = pd.DataFrame(self.caminhoes)
        df.to_csv("data/caminhoes.csv", index=False)
        print("Relatório de caminhões salvo em data/caminhoes.csv")

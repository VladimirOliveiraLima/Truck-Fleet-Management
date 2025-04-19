from src.frota.manutencao_manager import ManutencaoManager

def test_manutencao():
    mm = ManutencaoManager()
    mm.registrar_manutencao("DEF-5678", "Filtro", 50000)
    assert mm.manutencoes[0]["Descrição"] == "Filtro"

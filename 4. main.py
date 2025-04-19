from src.frota.frota_manager import FrotaManager
from src.frota.viagem_manager import ViagemManager
from src.frota.manutencao_manager import ManutencaoManager

def main():
    frota = FrotaManager()
    viagem = ViagemManager()
    manutencao = ManutencaoManager()

    # Cadastra caminhão
    frota.cadastrar_caminhao("ABC-1234", "Scania", 2020)
    frota.cadastrar_caminhao("DEF-5678", "Volvo", 2022)

    # Registra viagem
    viagem.registrar_viagem("ABC-1234", "São Paulo", "Curitiba", 410, 100)

    # Registra manutenção
    manutencao.registrar_manutencao("DEF-5678", "Troca de óleo", 30000)

    # Gera relatórios
    frota.gerar_relatorio()
    viagem.gerar_relatorio()
    manutencao.gerar_relatorio()

if __name__ == "__main__":
    main()

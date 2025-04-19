from src.frota.viagem_manager import ViagemManager

def test_viagem():
    vm = ViagemManager()
    vm.registrar_viagem("ABC-1234", "A", "B", 100, 20)
    assert len(vm.viagens) == 1

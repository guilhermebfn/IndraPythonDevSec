from SerVivo import SerVivo

class Monstro(SerVivo):
    tipo: str

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, tipo: str) -> None:
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo = tipo
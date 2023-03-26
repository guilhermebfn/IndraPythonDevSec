from Monstro import Monstro

class Goblin(Monstro):
    pontos_de_inteligencia: int

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, tipo: str, pontos_de_inteligencia: int) -> None:
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.pontos_de_inteligencia = pontos_de_inteligencia
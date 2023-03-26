from Monstro import Monstro

class Lobo(Monstro):
    pontos_de_forca: int

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, tipo: str, pontos_de_forca: int) -> None:
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.pontos_de_forca = pontos_de_forca
from SerVivo import SerVivo

class Personagem(SerVivo):
    nome: str

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, nome: str) -> None:
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.nome = nome
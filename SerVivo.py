class SerVivo:
    pontos_de_vida: int
    pontos_de_ataque: int

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int) -> None:
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_ataque = pontos_de_ataque

    def atacar(self, ser_vivo):
        ser_vivo.receber_dano(self.pontos_de_ataque)

    def receber_dano(self, dano):
        self.pontos_de_vida = max(self.pontos_de_vida - dano, 0)

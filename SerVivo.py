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


class Personagem(SerVivo):
    nome: str

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, nome: str) -> None:
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.nome = nome


class Monstro(SerVivo):
    tipo: str

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, tipo: str) -> None:
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo = tipo
    

class Lobo(Monstro):
    pontos_de_forca: int

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, tipo: str, pontos_de_forca: int) -> None:
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.pontos_de_forca = pontos_de_forca


class Goblin(Monstro):
    pontos_de_inteligencia: int

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, tipo: str, pontos_de_inteligencia: int) -> None:
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.pontos_de_inteligencia = pontos_de_inteligencia

personagem = Personagem(100, 20, "Guilherme")
goblin = Goblin(80, 30, "goblin", 10)

goblin.atacar(personagem)
goblin.atacar(personagem)
goblin.atacar(personagem)
print(personagem.pontos_de_vida)

personagem.atacar(goblin)
print(goblin.pontos_de_vida)
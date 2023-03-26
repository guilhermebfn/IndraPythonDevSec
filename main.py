from Personagem import Personagem
from Goblin import Goblin
from Lobo import Lobo

personagem = Personagem(100, 20, "Guilherme")
goblin = Goblin(80, 30, "goblin", 10)
lobo = Lobo(50, 25, "cinzento", 30)

goblin.atacar(personagem)
lobo.atacar(personagem)
goblin.atacar(personagem)
print(personagem.pontos_de_vida)

personagem.atacar(goblin)
print(goblin.pontos_de_vida)

personagem.atacar(lobo)
print(lobo.pontos_de_vida)

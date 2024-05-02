from pokemon import Pokemon

charmander = Pokemon("1", "Charmander",
                     ["Ember", "Scratch"],
                     0.5, 5)

squirtle = Pokemon("2", "Squirtle",
                   ["Duchazo", "Burbuja"],
                   0.5, 5)

pikachu : Pokemon

pikachu = Pokemon("3", "Pikachu",
                  ["Impactrueno", "Ataque rapido"],
                  0.5, 5)

print(charmander.skills)
pikachu.name = "Ratita"

print(pikachu.name)

quantidade = int(input())
pokemons = []
for i in range(quantidade):
    pokemons.append(input())

pokemons = set(pokemons)
total = 151 - len(pokemons)
print('Falta(m) %d pomekon(s).' % total)
adults = filter(lambda p: p.age >= 18, persons)
names = map(lambda p: p.name, adults)

# Als list comprehension:

names = [ p.name for p in persons if p.age >= 18 ]

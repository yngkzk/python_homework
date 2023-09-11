names = ['Sasha', 'Ilya', 'Galya', 'Igor', 'Ilya', 'Milek', 'Dilya', 'Galya']
imposters = []

for i in range(len(names)):
    suspect = names.count(names[i])
    if suspect >= 2:
        imposters.append(names[i])

print(imposters)

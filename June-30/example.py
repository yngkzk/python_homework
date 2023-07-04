sentence = 'She sells seashells by the seashore, The shells she sells are surely seashells'
value = sentence.find('seashells')
print(value)

value2 = sentence.find('seashells', 0, 9)
print(value2)

word = 'hallo'
wo = word.rjust(10, '-')
rd = wo.ljust(15, '-')
print(rd)

name = 'Bla Blanov Blanovich'
result = name.split()
print(result)
print(len(result))

newresult = ', '.join(result)
print(newresult)

space = '      hallo      \n'
print(space)
cut = space.strip()
print(cut)

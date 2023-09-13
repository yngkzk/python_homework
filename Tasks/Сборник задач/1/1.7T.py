# 1.7. Дана длина ребра куба. Найти площадь грани, площадь полной поверхности и объем этого куба.

a = 4

V_cube = a ** 3
S_side = a ** 2
S_total = S_side * 6

print('Side - %s m'
      '\nSide area - %s m,'
      '\nVolume - %s m,'
      '\nTotal surface area - %s m' % (a, S_side, V_cube, S_total))

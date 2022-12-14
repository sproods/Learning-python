#Character picture grid

#función que imprime la forma
def heart(pattern):
    tamX = len(pattern)
    tamY = len(pattern[1])
    
    print('\n')
    for y in range(tamY):
        for x in range(tamX):
            if x < tamX - 1:
                print(pattern[(-1) * (x + 1)][y], end='')
            elif x == tamX - 1:
                print(pattern[(-1) * (x + 1)][y])


#forma
grid = [['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]
    
#llamada a la función heart
heart(grid)
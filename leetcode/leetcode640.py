def solveEquation(equation):
    equation = equation.replace('-', '+-')
    left = equation.split('=')[0]
    right = equation.split('=')[1]
    x = 0
    cons = 0
    # 左x右常
    for i in left.split('+'):
        if i != '':
            if 'x' not in i:
                cons -= int(i)
            elif not i.isdigit() and len(i) > 1:
                x += int(i.split('x')[0] if i.split('x')[0] != '-' else -1)
            elif not i.isdigit() and len(i) == 1:
                x += 1

    for i in right.split('+'):
        if i != '':
            if 'x' not in i:
                cons += int(i)
            elif not i.isdigit() and len(i) > 1:
                x -= int(i.split('x')[0] if i.split('x')[0] != '-' else -1)
            elif not i.isdigit() and len(i) == 1:
                x -= 1

    if x == 0 and cons == 0:
        return 'Infinite solutions'

    if x == 0 and cons != 0:
        return 'No solution'

    return 'x=' + str(cons // x)


# print(solveEquation(equation="x+5-3+x=6+x-2"))
print(solveEquation(equation="-x=-1"))

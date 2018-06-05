import checkers

tablero = checkers.Checkers()

for x in tablero.get_table():
    print(*x)

tablero.move_piece('J',2)

print('')
for x in tablero.get_table():
    print(*x)
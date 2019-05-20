import random 
options = ['piedra', 'papel', 'tijeras']
pc = random.choice(options) 
print('¿Cómo te llamas?')
name = input()
print('Hola ' + name + '. Bienvenido al juego de piedra, papel o tijeras')

play= True

while play:

    player = input('Elije piedra, papel o tijeras: ')

    if player == 'papel':
        if pc == 'papel':
            print("Ambos sacamos papel. EMPATE")
        elif pc == 'tijeras':
            print("Yo saque tijeras. PIERDES")
        elif pc == 'piedra':
            print("Yo saque piedra. Papel le gana a piedra. GANASTE")

    if player == 'tijeras':
        if pc == 'tijeras':
            print("Ambos sacamos papel. EMPATE")
        elif pc == 'piedra':
            print("Yo saque piedra. Piedra rompe tijeras. PIERDES")
        elif pc == 'papel':
            print("Yo saque papel. Tijeras cortan papel. GANASTE")

    if player == 'piedra':
        if pc == 'piedra':
            print("Ambos sacamos piedra. EMPATE")
        elif pc == 'papel':
            print("Yo saque papel. Papel envuelve a la piedra. PIERDES")
        elif pc == 'tijeras':
            print("Yo saque tijeras. Piedra rompe las tijeras. GANASTE")
    seguir = input("¿Quieres seguir jugando? (s/n): ")
    if seguir == "n":
        play = False
        print("Muchas gracias por jugar " + name + " :)") 
    elif seguir == "s":
        play = True
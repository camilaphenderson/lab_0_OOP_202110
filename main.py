from cards import Cards
from player import Player 
cards = Cards.create_cards(15)
n = int(input('Ingrese numero de jugadores :'))
players = []
def create_player(n):
    if n>4 or n<3 :
        raise ValueError ('Tienen que ser 3 o 4 jugadores')
    else :
        for i in range(n):
            name = 'player ' + str(i+1)
            print(name)
            players.append(Player(name,2,2))
            i+=1
create_player(n)

def inicial_menu():
    print('\Elija que carta quiere jugar')
    print('1.acción general')
    print('2.acción de personaje')
    return int(input())

def menu_general():
    print('Seleccione que acción desea realizar')
    print('1. Ingreso')
    print('2. Ayuda extranjera')
    print('3. Golpe')
    return int(input())
def menu_characters():
    print('Seleccione que personaje desea usar')
    print('1. Duque')
    print('2. Asesino')
    print('3. Capitán')
    print('4. Embajador')
    return int(input())

def menu():
    selection = inicial_menu()
    if selection == 1:
        selection = menu_general()
        return selection
    if selection == 2:
        selection = menu_characters()
        return selection
    else:
        print('Ingrese una opción válida')
    

print(menu())
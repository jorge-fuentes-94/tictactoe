def visual(game):
    print(f"\n{game[1]}       {game[2]}       {game[3]}\n{game[4]}       {game[5]}       {game[6]}\n{game[7]}       {game[8]}       {game[9]}\n")

def check_win(game,player):
    player_victory = ""
    winner = False
    fields_to_check = ["".join(game[1]+game[2]+game[3]),"".join(game[4]+game[5]+game[6]),"".join(game[7]+game[8]+game[9]),"".join(game[1]+game[4]+game[7]),"".join(game[2]+game[5]+game[8]),"".join(game[3]+game[6]+game[9]),"".join(game[1]+game[5]+game[9]),"".join(game[3]+game[5]+game[7])]
    if player == 1:
        player_victory = "XXX"
    else:
        player_victory = "OOO"

    for field in fields_to_check:
        winner = check_win_conditions(player_victory,field)
        if winner == True:
            return winner

def check_win_conditions(player_victory,field_to_check):
    return player_victory == field_to_check

def isNumber(input):
    if input <=0 or input >9 or type(input) != int:
        print("Ese número no me vale. Introduce un número del 1 al 9.")
        return False
    return True
            
def check_repeated(input,game):
    if game[input] == "X" or game[input] == "O":
        print ("Ese espacio ya ha sido ocupado, vuelve a intentarlo.")
        return 0
    else:
        return 1

def play(game,player):
    X = 0
    check_number = False
    while X == 0 and check_number == False:
        player_input = int(input(f"Jugador {player}, introduce el espacio que quieres ocupar: "))
        check_number = isNumber(player_input)
        X = check_repeated(player_input, game)
    if player == 1:
        game[player_input] = "X"
    else: 
        game[player_input] = "O"
    return game

def intro():
    print("Vamos a jugar al tres en raya. En este juego tomaréis turnos eligiendo uno de los huecos. Para ganar hay que tener tres espacios escogidos juntos, ya sea en vertical, horizontal o diagonal.")
    print("En caso de llenarse el tablero y no quedar huecos libres, el juego acaba en empate.")
    print("El jugador 1 usará X y el jugador 2 usará O. En cada turno debes escribir el número correspondiente al espacio que quieres ocupar.")
    visual(game)

game = ["0","1","2","3","4","5","6","7","8","9"]
round = 1
winner = False
players = [1,2]

intro()

while round <5:
    for player in players:
        game = play(game,player)
        visual(game)
        if round >= 3:
            winner = check_win(game,player)
            if winner == True:
                print (f"¡El jugador {player} gana!¡Bien jugado!")
                exit()    
    print("¡Nadie gana! ¡Siguiente ronda!")
    round += 1
print("¡Empate técnico! ¡Nadie gana!")

    
    
    
    
    
   
       

   
        


    



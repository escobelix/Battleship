import background_V4_1 as bg

tablero_player = bg.tabla()
tablero_maquina = bg.tabla()
tablero_player_disparo = bg.tabla()
tablero_maquina_disparo = bg.tabla()

bg.inicializar(tablero_player, tablero_maquina)


while bg.cuenta_vidas(tablero_maquina, tablero_player) == True:

    bg.disparar_player(tablero_maquina, tablero_player_disparo)

    bg.disparar_maquina(tablero_player, tablero_maquina_disparo)
    

   
    


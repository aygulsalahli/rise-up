import manual_controls
import movements

if manual_controls.user_input == 'w':
    movements.move('forward')
elif manual_controls.user_input == 's':
    movements.move('reverse')
elif manual_controls.user_input == 'a':
    movements.turn('left')
elif manual_controls.user_input == 'd':
    movements.turn('right')
elif manual_controls.user_input == 'u':
    movements.turn('u_turn')
elif manual_controls.user_input == 'r':
    movements.lift('up')
elif manual_controls.user_input == 'f':
    movements.lift('down')
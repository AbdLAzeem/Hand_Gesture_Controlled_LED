import pyfirmata

def connect_arduino(comport='COM11'):
    try:
        board = pyfirmata.Arduino(comport)
        print(f"Connected to Arduino on {comport}")
        return board
    except Exception as e:
        print(f"Error: Could not connect to Arduino on {comport}. {e}")
        return None

def setup_leds(board):
    if board is None:
        return []
    try:
        leds = [
            board.get_pin('d:8:o'),
            board.get_pin('d:9:o'),
            board.get_pin('d:10:o'),
            board.get_pin('d:11:o'),
            board.get_pin('d:12:o')
        ]
        return leds
    except Exception as e:
        print(f"Error setting up LED pins: {e}")
        return []

def update_leds(leds, fingerUpCount):
    if not leds:
        return
    for i in range(5):
        try:
            if i < fingerUpCount:
                leds[i].write(1) 
            else:
                leds[i].write(0)
        except Exception as e:
            print(f"Error writing to LED {i+1}: {e}")

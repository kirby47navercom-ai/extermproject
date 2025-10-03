import tkinter as tk
import time

root = tk.Tk()

screen_width = 1536
screen_height = 864




def ingame(game_manager):
    global running
    running = True

    global frame_time
    frame_time = 0.0
    current_time = time.time()
    game_manager.update(frame_time)
    game_manager.render()
    while running:
        frame_time = time.time() - current_time
        current_time += frame_time


    pass

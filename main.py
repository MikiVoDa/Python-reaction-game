import tkinter as tk
import random
import time


def start_joc():
    canvas.itemconfig(red_dot, fill="red")
    root.after(random.randint(1000, 5000), turn_green)


def turn_green():
    global start_time
    canvas.itemconfig(red_dot, fill="green")
    start_time = time.time()


def on_click(event):
    if canvas.itemcget(red_dot, "fill") == "green":
        reaction_time = time.time() - start_time
        show_reaction_time(reaction_time)


def show_reaction_time(reaction_time):
    canvas.delete(red_dot)
    canvas.create_text(200, 200,
                       text=f"Timp de reactie: {reaction_time:.3f} secunde",
                       fill="black",
                       font=("Helvetica", 20))
    root.after(3000, start_joc)


# main

root = tk.Tk()
root.title("Test de Reactie")
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

red_dot = canvas.create_oval(150, 150, 250, 250, fill="red")
canvas.bind("<Button-1>", on_click)

start_joc()
root.mainloop()

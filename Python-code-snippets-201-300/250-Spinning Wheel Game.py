"""250-Spinning Wheel Game

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements: None.

Origin:
https://gist.github.com/shiracamus/071b6a7d4dfc7f1640aff782c4537090

This is not very PEP8. I haven't changed anything.
"""
import tkinter as tk
import math

class Board:
    def __init__(self, divide, top=90):
        self.divide = divide
        self.top = top
        self.offset = top - 360 // divide // 2

    def position(self, angle):
        return (angle - self.offset) % 360 * self.divide // 360

class Ball:
    def __init__(self, step, top=90):
        self.step = step
        self.angle = top

    def move(self):
        self.angle += self.step

class Roulette:
    def __init__(self, divide, step):
        self.board = Board(divide)
        self.ball = Ball(step)
        self.rolling = True

    def start_stop(self):
        self.rolling = not self.rolling

    def update(self):
        self.rolling and self.ball.move()

class RouletteView:
    FONT = ("Helvetica", 50, "bold")
    def __init__(self, master, roulette):
        self.roulette = roulette

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        angle = 360 // roulette.board.divide
        for i in range(roulette.board.divide):
            arc = (angle * i + roulette.board.offset) % 360
            self.canvas.create_arc(75, 75, 425, 425,
                start=arc, extent=angle, fill="white", width=2)
            txt = (angle * i + roulette.board.top) % 360
            x = ((200 * (3**(1 / 2))) / 3) * math.cos(math.radians(txt)) + 250
            y = -100 * math.sin(math.radians(txt)) + 250
            self.canvas.create_text(x, y,
                text=str(roulette.board.position(txt) + 1),
                font=self.FONT, fill="blue")

        self.update()

    def update(self):
        angle = self.roulette.ball.angle
        if self.roulette.rolling:
            self.canvas.delete("ball")
            self.canvas.delete("stop")
            self.canvas.create_line(250, 250,
                +125 * math.cos(math.radians(angle)) + 250,
                -125 * math.sin(math.radians(angle)) + 250,
                fill="red", width=5, tag="ball")
        else:
            self.canvas.create_text(450, 450,
                text=str(self.roulette.board.position(angle) + 1),
                font=self.FONT, fill="blue", tag="stop")

class Application(tk.Frame):
    DIVIDE = 6
    STEP = -10
    UPDATE = 10

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("500x500")
        master.title("Press space bar")

        self.model = roulette = Roulette(divide=self.DIVIDE, step=self.STEP)
        self.view = RouletteView(master, roulette)
        self.master.bind("<space>", lambda *args: roulette.start_stop())
        self.master.after(self.UPDATE, self.update)

    def update(self):
        self.model.update()
        self.view.update()
        self.master.after(self.UPDATE, self.update)

def main():
    master = tk.Tk()
    app = Application(master)
    app.mainloop()

if __name__ == "__main__":
    main()

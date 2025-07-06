import tkinter as tk
import model

LABEL_O_SHOW = "O"
LABEL_X_SHOW = "X"
LABEL_UNSET_SHOW = "_"

class GameFrame(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.reset()

    def btnpressed(self, row, col):
        self.model.pick_pos(row, col)
        for i in range(3):
            for j in range(3):
                if self.model.board[i][j] == model.LABEL_X:
                    self.btns[(i, j)]["text"] = LABEL_X_SHOW
                elif self.model.board[i][j] == model.LABEL_O:
                    self.btns[(i, j)]["text"] = LABEL_O_SHOW
                else:
                    self.btns[(i, j)]["text"] = LABEL_UNSET_SHOW
        if self.model.game_reset is True:
            self.model.reset()
            self.reset()

    def reset(self):
        self.btns = {}
        for row in range(3):
            for col in range(3):
                btn = GameButton(self, row, col)
                btn.grid(row=row, column=col)
                self.btns[(row, col)] = btn
        self.model = model.Game()

class GameButton(tk.Button):
    def __init__(self, root, row, col):
        tk.Button.__init__(self, root, text="_", width=10, height=5)
        self.row = row
        self.col = col
        self["command"] = self.press
        self.delegate = root

    def press(self):
        if self["text"] == "_":
            self.delegate.btnpressed(self.row, self.col)
        else:
            pass

root = tk.Tk()
root.title("OOXX")
GameFrame(root).pack()
tk.mainloop()

LABEL_O = 1
LABEL_X = -1

class Game:
    def __init__(self):
        self.reset()

    def pick_pos(self, row, col):
        if self.round % 2 == 0:
            label = LABEL_O
        else:
            label = LABEL_X
        self.round = self.round + 1
        self.board[row][col] = label
        self.check_winner()


    def check_winner(self):
        # 橫的
        # 固定board[0][0] 看 board[0][1] 和 board[0][2] 是否跟board[0][0]一樣
        i = 0
        while i < 3:
            # 如果這列的第一個位置不是0
            if not self.board[i][0] == 0:
                # 他們三個是一樣的
                if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                    print(i, "WIN")
                    self.game_reset = True
            i = i + 1

        # 直的
        # 固定board[0][0] 看 board[1][0] 和 board[2][0] 是否跟board[0][0]一樣

        i = 0
        while i < 3:
            # 這一個直行的第一個不是0
            if not self.board[0][i] == 0:
                # 他們三個是一樣的
                if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                    print(i, "WIN")
                    # reset
                    self.game_reset = True
            i = i + 1

        # 斜的
        # 00 11 22
        # 02 11 20
        if not self.board[1][1] == 0:
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                print("左上到右下WIN")
                self.game_reset = True
            if self.board[0][2] == self.board[1][1] == self.board[2][0]:
                print("右上到左下WIN")
                self.game_reset = True

    def reset(self):
        self.round = 0
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.game_reset = False

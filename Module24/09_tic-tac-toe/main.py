class Tic_Tac_Toe:

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def draw_board(self):
        print("-------------")
        for i_num in range(3):
            print("|", self.board[0 + i_num * 3], "|", self.board[1 + i_num * 3], "|", self.board[2 + i_num * 3], "|")
            print("-------------")

    def take_input(self, player_token):
        flag = False
        while not flag:
            player_answer = input(f'Куда поставим {player_token}? ')
            try:
                player_answer = int(player_answer)
            except:
                print('Вы уверенны что ввели число?')
                continue
            if player_answer >= 1 and player_answer <= 9:
                if (str(self.board[player_answer - 1]) not in 'XO'):
                    self.board[player_answer - 1] = player_token
                    flag = True
                else:
                    print('Эта клеточка уже занята')
            else:
                print('Нужно вводить число от 1 до 9')

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False

    def game(self):
        count = 0
        win = False
        while not win:
            self.draw_board()
            if count % 2 == 0:
                self.take_input('X')
            else:
                self.take_input('O')
            count += 1

            if count > 4:
                tmp = self.check_win()
                if tmp:
                    print(tmp, 'Выиграл')
                    win = True
                    break
            if count == 9:
                print('Ничья')
                break


pleyer = Tic_Tac_Toe()
pleyer.game()

# зачёт!

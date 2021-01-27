# Name: Wade Nelson
# Date: 6/4/2020
# Description: Gess

# used for converting the algebraic notation of the external board to the row-column structure of the internal board
rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']


class GessGame:
    """represents a game of Gess with a board and pieces"""

    def __init__(self):
        """
        initalizes the board as a 2 dimensional list with an initial configuration of stones
        initliazes a dictionary of every potential piece
        initalizes the player turn tracker
        initalizes the game state
        loads the board state into the dictionary of piece objects
        """
        self._board = [
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # 00    20
            [4, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 0, 4],  # 01    19
            [4, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 2, 4],  # 02    18
            [4, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 0, 4],  # 03    17
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 04    16
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 05    15
            [4, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 4],  # 06    14
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 07    13
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 08    12
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 09    11
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 10    10
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 11    09
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 12    08
            [4, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 4],  # 13    07
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 14    06
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 15    05
            [4, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 4],  # 16    04
            [4, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 4],  # 17    03
            [4, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 4],  # 18    02
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # 19    01
            # 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19
            # 0A 0B 0C 0D 0E 0F 0G 0H 0I 0J 0K 0L 0M 0N 0O 0P 0Q 0R 0S 0T
        ]
        self._prev_board = self._board.copy()
        self._piece = {}
        self._player_turn = 'BLACK'
        self._game_state = 'UNFINISHED'
        self.board_to_pieces()

    def board_to_pieces(self):
        """takes the layout of stones on the board and loads the configuration of the stones into piece objects"""
        for i in range(18, 0, -1):
            for j in range(1, 19):
                row = 18 - j
                col = i - 1
                self._piece[cols[i] + rows[j]] = Piece(
                    self._board[row + 1][col + 1],  # middle         (mi)
                    self._board[row + 0][col + 1],  # up             (up)
                    self._board[row + 2][col + 1],  # down           (do)
                    self._board[row + 1][col + 0],  # left           (le)
                    self._board[row + 1][col + 2],  # right          (ri)
                    self._board[row + 0][col + 2],  # upper right    (ur)
                    self._board[row + 2][col + 2],  # lower right    (lr)
                    self._board[row + 2][col + 0],  # lower left     (ll)
                    self._board[row + 0][col + 0],  # upper left     (ul)
                )

    def get_game_state(self):
        """returns the current game state"""
        return self._game_state

    def resign_game(self):
        """resigns game"""
        if self._player_turn == 'BLACK':
            self._game_state = 'WHITE_WON'
        if self._player_turn == 'WHITE':
            self._game_state = 'BLACK_WON'

    def print_board(self):
        """displays the board for debug purposes"""
        if self._player_turn == 'BLACK':
            # or self._player_turn =='WHITE'
            row = 20
            for i in self._board:
                line = ''
                for j in i:
                    if j == 0:
                        line += '|' + ' '
                    if j == 1:
                        line += '|b'
                    if j == 2:
                        line += '|w'
                    if j == 4:
                        line += '  '
                    # else:
                    # line += str(j) + '  '
                if row < 10:
                    print(str(row) + '   ' + line)
                else:

                    print(str(row) + '  ' + line)
                row -= 1
            print('     A B C D E F G H I J K L M N O P Q R S T')

        if self._player_turn == 'WHITE':
            row = 1
            for i in reversed(self._board):
                line = ''
                for j in reversed(i):
                    if j == 0:
                        line += '|' + ' '
                    if j == 1:
                        line += '|b'
                    if j == 2:
                        line += '|w'
                    if j == 4:
                        line += '  '
                    # else:
                    # line += str(j) + '  '
                if row < 10:
                    print(str(row) + '   ' + line)
                else:

                    print(str(row) + '  ' + line)
                row += 1
            print('     T S R Q P O N M L K J I H G F E D C B A')

    def make_move(self, start, stop):
        """makes a move"""

        prev_board = [x[:] for x in self._board]
        row = start[1::]
        col = start[0]
        black_ring = None
        white_ring = None

        # if there are both black and white stones in the prospective piece's configuration, the piece is invalid
        if 1 in self._piece[start].get_cf() and 2 in self._piece[start].get_cf():
            return False

        # The following 8 blocks look in all 8 directions and log all possible legal moves

        # up
        if self._piece[start].get_up()[1] == 1 and self._player_turn == 'BLACK' or self._piece[start].get_up()[
            1] == 2 and self._player_turn == 'WHITE':
            row = str(int(start[1::]) + 1)
            col = start[0]
            if self._piece[start].get_mi() == 0:
                moves = 2
            else:
                moves = 18
            try:
                while self._piece[col + row].get_up() == (0, 0, 0) and moves > 0:
                    self._piece[start].set_mo(col + row)
                    row = str(int(row) + 1)
                    col = col
                    moves -= 1
            except KeyError:
                pass
            self._piece[start].set_mo(col + row)
            # print(self._piece[start].get_mo())

        # down
        if self._piece[start].get_do()[1] == 1 and self._player_turn == 'BLACK' or self._piece[start].get_do()[
            1] == 2 and self._player_turn == 'WHITE':
            row = str(int(start[1::]) - 1)
            col = start[0]
            if self._piece[start].get_mi() == 0:
                moves = 2
            else:
                moves = 18
            try:
                while self._piece[col + row].get_do() == (0, 0, 0) and moves > 0:
                    self._piece[start].set_mo(col + row)
                    row = str(int(row) - 1)
                    col = col
                    moves -= 1
            except KeyError:
                pass
            self._piece[start].set_mo(col + row)
            # print(self._piece[start].get_mo())

        # left
        if self._piece[start].get_le()[1] == 1 and self._player_turn == 'BLACK' or self._piece[start].get_le()[
            1] == 2 and self._player_turn == 'WHITE':
            row = start[1::]
            col = chr((ord(start[0]) - 1))
            if self._piece[start].get_mi() == 0:
                moves = 2
            else:
                moves = 18
            try:
                while self._piece[col + row].get_le() == (0, 0, 0) and moves > 0:
                    self._piece[start].set_mo(col + row)
                    row = row
                    col = chr((ord(col) - 1))
                    moves -= 1
            except KeyError:
                pass
            self._piece[start].set_mo(col + row)
            # print(self._piece[start].get_mo())

        # right
        if self._piece[start].get_ri()[1] == 1 and self._player_turn == 'BLACK' or self._piece[start].get_ri()[
            1] == 2 and self._player_turn == 'WHITE':
            row = start[1::]
            col = chr((ord(start[0]) + 1))
            if self._piece[start].get_mi() == 0:
                moves = 2
            else:
                moves = 18
            try:
                while self._piece[col + row].get_ri() == (0, 0, 0) and moves > 0:
                    self._piece[start].set_mo(col + row)
                    row = row
                    col = chr((ord(col) + 1))
                    moves -= 1
            except KeyError:
                pass
            self._piece[start].set_mo(col + row)
            # print(self._piece[start].get_mo())

        # upper-right
        if self._piece[start].get_ur()[2] == 1 and self._player_turn == 'BLACK' or self._piece[start].get_ur()[
            2] == 2 and self._player_turn == 'WHITE':
            row = str(int(start[1::]) + 1)
            col = chr((ord(start[0]) + 1))
            if self._piece[start].get_mi() == 0:
                moves = 2
            else:
                moves = 18
            try:
                while self._piece[col + row].get_ur() == (0, 0, 0, 0, 0) and moves > 0:
                    self._piece[start].set_mo(col + row)
                    row = str(int(row) + 1)
                    col = chr((ord(col) + 1))
                    moves -= 1
            except KeyError:
                pass
            self._piece[start].set_mo(col + row)
            # print(self._piece[start].get_mo())

        # lower-right
        if self._piece[start].get_lr()[2] == 1 and self._player_turn == 'BLACK' or self._piece[start].get_lr()[
            2] == 2 and self._player_turn == 'WHITE':
            row = str(int(start[1::]) - 1)
            col = chr((ord(start[0]) + 1))
            if self._piece[start].get_mi() == 0:
                moves = 2
            else:
                moves = 18
            try:
                while self._piece[col + row].get_lr() == (0, 0, 0, 0, 0) and moves > 0:
                    self._piece[start].set_mo(col + row)
                    row = str(int(row) - 1)
                    col = chr((ord(col) + 1))
                    moves -= 1
            except KeyError:
                pass
            self._piece[start].set_mo(col + row)
            # print(self._piece[start].get_mo())

        # lower-left
        if self._piece[start].get_ll()[2] == 1 and self._player_turn == 'BLACK' or self._piece[start].get_ll()[
            2] == 2 and self._player_turn == 'WHITE':
            row = str(int(start[1::]) - 1)
            col = chr((ord(start[0]) - 1))
            if self._piece[start].get_mi() == 0:
                moves = 2
            else:
                moves = 18
            try:
                while self._piece[col + row].get_ll() == (0, 0, 0, 0, 0) and moves > 0:
                    self._piece[start].set_mo(col + row)
                    row = str(int(row) - 1)
                    col = chr((ord(col) - 1))
                    moves -= 1
            except KeyError:
                pass
            self._piece[start].set_mo(col + row)
            # print(self._piece[start].get_mo())

        # upper-left
        if self._piece[start].get_ul()[2] == 1 and self._player_turn == 'BLACK' or self._piece[start].get_ul()[
            2] == 2 and self._player_turn == 'WHITE':
            row = str(int(start[1::]) + 1)
            col = chr((ord(start[0]) - 1))
            if self._piece[start].get_mi() == 0:
                moves = 2
            else:
                moves = 18
            try:
                while self._piece[col + row].get_ul() == (0, 0, 0, 0, 0) and moves > 0:
                    self._piece[start].set_mo(col + row)
                    row = str(int(row) + 1)
                    col = chr((ord(col) - 1))
                    moves -= 1
            except KeyError:
                pass
            self._piece[start].set_mo(col + row)
            # print(self._piece[start].get_mo())

        # if the intended move is within the starting piece's potential legal moves
        if stop in self._piece[start].get_mo():
            stop_col = cols.index(stop[0])
            stop_row = 20 - int(stop[1::])
            start_col = cols.index(start[0])
            start_row = 20 - int(start[1::])

            # store the start piece's initial configuration
            temp_mi = self._board[start_row][start_col]
            temp_up = self._board[start_row - 1][start_col]
            temp_do = self._board[start_row + 1][start_col]
            temp_le = self._board[start_row][start_col - 1]
            temp_ri = self._board[start_row][start_col + 1]
            temp_ur = self._board[start_row - 1][start_col + 1]
            temp_lr = self._board[start_row + 1][start_col + 1]
            temp_ll = self._board[start_row + 1][start_col - 1]
            temp_ul = self._board[start_row - 1][start_col - 1]

            # remove the starting piece
            self._board[start_row][start_col] = 0
            self._board[start_row - 1][start_col] = 0
            self._board[start_row + 1][start_col] = 0
            self._board[start_row][start_col - 1] = 0
            self._board[start_row][start_col + 1] = 0
            self._board[start_row - 1][start_col + 1] = 0
            self._board[start_row + 1][start_col + 1] = 0
            self._board[start_row + 1][start_col - 1] = 0
            self._board[start_row - 1][start_col - 1] = 0

            # move the starting piece to the intended position
            self._board[stop_row][stop_col] = temp_mi
            self._board[stop_row - 1][stop_col] = temp_up
            self._board[stop_row + 1][stop_col] = temp_do
            self._board[stop_row][stop_col - 1] = temp_le
            self._board[stop_row][stop_col + 1] = temp_ri
            self._board[stop_row - 1][stop_col + 1] = temp_ur
            self._board[stop_row + 1][stop_col + 1] = temp_lr
            self._board[stop_row + 1][stop_col - 1] = temp_ll
            self._board[stop_row - 1][stop_col - 1] = temp_ul

            # update all pieces to represent the layout of the new board
            self.board_to_pieces()

            # remove any stones that fell into the out-of-bounds area during the move
            for i in range(20):
                self._board[0][i] = 4
                self._board[i][19] = 4
                self._board[19][i] = 4
                self._board[i][0] = 4

            # clean up any out-of-bounds squares (4's) that got moved onto the board
            for i in range(1, 19):
                for j in range(1, 19):
                    if self._board[i][j] == 4:
                        self._board[i][j] = 0

            # look for rings
            for piece in self._piece:
                if self._piece[piece].get_cf() == [[1, 1, 1], [1, 0, 1], [1, 1, 1]]:
                    black_ring = True
                if self._piece[piece].get_cf() == [[2, 2, 2], [2, 0, 2], [2, 2, 2]]:
                    white_ring = True

            # if black has made a move that would result in no black ring, go back to the previous board state
            if black_ring is None and self._player_turn == 'BLACK':
                self._board = [i[:] for i in prev_board]
                self.board_to_pieces()
                # print('Cannot make a move that leaves the player with no ring')
                return False

            # if white has made a move that would result in no white ring, go back to the previous board state
            if white_ring is None and self._player_turn == 'WHITE':
                self._board = [i[:] for i in prev_board]
                self.board_to_pieces()
                # print('Cannot make a move that leaves the player with no ring')
                return False

            # if black has made a move that results in no white ring, black wins
            if black_ring is None and self._player_turn == 'WHITE':
                self._game_state = 'WHITE_WON'
                self._player_turn = 'NONE'

            # if white has made a move that results in no black ring, white wins
            if white_ring is None and self._player_turn == 'BLACK':
                self._game_state = 'BLACK_WON'
                self._player_turn = 'NONE'

            # take turns
            if self._player_turn == 'BLACK':
                self._player_turn = 'WHITE'
            else:
                self._player_turn = 'BLACK'

            # self.print_board()
            # print(self._player_turn)
            # print(self._game_state)
            return True

        # no legal moves
        else:
            return False


class Piece:
    """represents a Piece with a 9 slot configuration"""

    def __init__(self, mi, up, do, le, ri, ur, lr, ll, ul):
        """middle (mi), upper (up), downward (do), left (le), right (ri), upper-right (ur), lower-right (lr),
        lower-left (ll), upper-left (ul), configuration (cf), and moves (mo) """
        self._mi = mi  # middle
        self._up = up  # up
        self._do = do  # down
        self._le = le  # left
        self._ri = ri  # right
        self._ur = ur  # upper-right
        self._lr = lr   #lower-right
        self._ll = ll   #lower-left
        self._ul = ul   #upper-left
        self._cf = [
            [ul, up, ur],
            [le, mi, ri],
            [ll, do, lr],
        ]
        self._mo = []

    def get_mi(self):
        """returns the middle slot's value"""
        return self._mi

    def get_up(self):
        """returns the upper row"""
        return (self._ul, self._up, self._ul)

    def get_do(self):
        """returns the downward row"""
        return (self._ll, self._do, self._lr)

    def get_le(self):
        """returns the left-most column"""
        return (self._ul, self._le, self._ll)

    def get_ri(self):
        """returns the right-most column"""
        return (self._ur, self._ri, self._lr)

    def get_ur(self):
        """returns the upper-right arrow"""
        return (self._ul, self._up, self._ur, self._ri, self._lr)

    def get_lr(self):
        """returns the lower-right arrow"""
        return (self._ur, self._ri, self._lr, self._do, self._ll)

    def get_ll(self):
        """returns the lower-left arrow"""
        return (self._lr, self._do, self._ll, self._le, self._ul)

    def get_ul(self):
        """returns the upper-left arrow"""
        return (self._ll, self._le, self._ul, self._up, self._ur)

    def get_cf(self):
        """returns the piece's configuration"""
        return self._cf

    def set_mo(self, mo):
        """appends a move to the piece's legal moves"""
        self._mo.append(mo)

    def get_mo(self):
        """returns the piece's legal moves"""
        return self._mo
class Reversi():

    def __init__(self, board_string='''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            '''):
        self.board = self.parse_board(board_string)
        self.player = 'b'
        self.directional_increments = {
                'east':       {'row':  0, 'column':  1},
                'west':       {'row':  0, 'column': -1},
                'north':      {'row': -1, 'column':  0},
                'south':      {'row':  1, 'column':  0},
                'north_east': {'row': -1, 'column':  1},
                'north_west': {'row': -1, 'column': -1},
                'south_west': {'row':  1, 'column': -1},
                'south_east': {'row':  1, 'column':  1},
            }
        self.directions = [
                'east', 'west', 'north', 'south', 'north_east', 'north_west',
                'south_west', 'south_east'
            ]

    def move(self, position):
        column, row = self.indexes_from_position(position)

        self.board[self.col_key(column)][self.row_key(row)] = self.player

        for direction in self.directions:
            if self.is_traversal_valid_for(direction, self.player, position):
                self.flip_pieces(direction, self.player, position)

        self.player = self.opponent()

        return True

    def opponent(self):
        return ({'b', 'w'} - {self.player}).pop()

    def parse_board(self, board_string):
        board = dict(A={}, B={}, C={}, D={}, E={}, F={}, G={}, H={})
        rows = board_string.strip().split("\n")
        board_ary = [i.strip().split(' ') for i in rows]
        for i, row in enumerate(board_ary):
            for j, cell in enumerate(row):
                column_letter = chr(j + 65)
                board[column_letter][i + 1] = cell
        return board

    def board_string(self):
        string = ''
        for i in range(1, 9):
            str_line = ''
            for c in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                str_line += ' ' + self.board[c][i]
            string += str_line.strip() + "\n"
        return string

    def increment_traversal(self, direction, col, row):
        return [
                col + self.directional_increments[direction]['column'],
                row + self.directional_increments[direction]['row']
            ]

    def indexes_from_position(self, position):
        return [ord(position[0]) - 65, int(position[1]) - 1]

    def col_key(self, n):
        return chr(n + 65)

    def row_key(self, n):
        return n + 1;

    def piece_at(self, column, row):
        return self.board[self.col_key(column)][self.row_key(row)]

    def continue_east(self, col, row):
        return col < 8

    def continue_west(self, col, row):
        return col > -1

    def continue_north(self, col, row):
        return row > 0

    def continue_south(self, col, row):
        return row < 9

    def continue_north_east(self, col, row):
        return col < 7 and row > 0

    def continue_north_west(self, col, row):
        return col > 0 and row > 0

    def continue_south_west(self, col, row):
        return col > 0 and row < 7

    def continue_south_east(self, col, row):
        return col < 7 and row < 7

    def continue_traversal(self, direction, col, row):
        return getattr(self, 'continue_' + direction)(col, row)

    def too_close_to_edge(self, direction, col, row):
        return (direction == 'east'       and col >= 7 or
                direction == 'west'       and col <= 0 or
                direction == 'north'      and row <= 1 or
                direction == 'south'      and row >= 7 or
                direction == 'north_east' and (col >= 7 or row <= 0)  or
                direction == 'north_west' and (col <= 0 or row <= 0)  or
                direction == 'south_east' and (col >= 7 or row >= 7))

    def is_traversal_valid_for(self, direction, color, position):
        column, row = self.indexes_from_position(position)

        if self.too_close_to_edge(direction, column, row):
            return False

        opposite_color_count = 0
        while self.continue_traversal(direction, column, row):
            column, row = self.increment_traversal(direction, column, row)

            piece = self.piece_at(column, row)
            if (color == piece or piece == '-'):
                break
            elif self.piece_at(column, row) != '-':
                opposite_color_count += 1
        if color == self.piece_at(column, row) and opposite_color_count >= 1:
            return True

        return False

    def is_move_valid(self, color, position):
        if self.board[position[0]][int(position[1])] != '-':
            return False

        for direction in self.directions:
            if self.is_traversal_valid_for(direction, color, position):
                return True

        return False

    def flip_pieces(self, direction, color, position):
        column, row = self.indexes_from_position(position)

        while True:
            column, row = self.increment_traversal(direction, column, row)

            next_piece = self.piece_at(column, row)
            self.board[chr(column + 65)][row + 1] = color

            if next_piece == color:
                break

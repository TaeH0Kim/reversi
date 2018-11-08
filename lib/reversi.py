class Reversi():

    def __init__(self, board_str='''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            '''):
        board = dict(A={}, B={}, C={}, D={}, E={}, F={}, G={}, H={})
        rows = board_str.strip().split("\n")
        board_ary = [i.strip().split(' ') for i in rows]
        for i, row in enumerate(board_ary):
            for j, cell in enumerate(row):
                column_letter = chr(j + 65)
                board[column_letter][i + 1] = cell
        self.board = board
        self.player = 'b'
        self.traversal_increments = {
                'east':       {'row_increment':  0, 'column_increment':  1},
                'west':       {'row_increment':  0, 'column_increment': -1},
                'north':      {'row_increment': -1, 'column_increment':  0},
                'south':      {'row_increment':  1, 'column_increment':  0},
                'north_east': {'row_increment': -1, 'column_increment':  1},
                'north_west': {'row_increment': -1, 'column_increment': -1},
                'south_west': {'row_increment':  1, 'column_increment': -1},
                'south_east': {'row_increment':  1, 'column_increment':  1},
            }
        self.directions = [
                'east', 'west', 'north', 'south', 'north_east', 'north_west',
                'south_west', 'south_east'
                ]


    def move(self, position):
        column = position[0]
        row = int(position[1])

        self.board[column][row] = self.player

        for direction in self.directions:
            if self.is_traversal_valid_for(direction, self.player, position):
                self.flip_pieces(direction, self.player, position)

        if self.player == 'b':
            self.player = 'w'
        else:
            self.player = 'b'

        return True

    def board_string(self):
        string = ''
        for i in range(1, 9):
            str_line = ''
            for c in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                str_line += ' ' + self.board[c][i]
            string += str_line.strip() + "\n"
        return string

    def col_key(self, n):
        return chr(n + 65)

    def row_key(self, n):
        return n + 1;

    def piece_at(self, column_index, row_index):
        return self.board[self.col_key(column_index)][self.row_key(row_index)]

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

    def too_close_to_edge(self, direction, col, row):
        return (direction == 'east'       and col >= 7 or
                direction == 'west'       and col <= 0 or
                direction == 'north'      and row <= 1 or
                direction == 'south'      and row >= 7 or
                direction == 'north_east' and (col >= 7 or row <= 0)  or
                direction == 'north_west' and (col <= 0 or row <= 0)  or
                direction == 'south_east' and (col >= 7 or row >= 7))

    def is_traversal_valid_for(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while getattr(self, 'continue_' + direction)(column_index, row_index):
            column_index += self.traversal_increments[direction]['column_increment']
            row_index += self.traversal_increments[direction]['row_increment']

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1
        if color == self.piece_at(column_index, row_index) and opposite_color_count >= 1:
            return True

        return False

    def is_move_valid(self, color, position):
        if self.board[position[0]][int(position[1])] != '-':
            return False

        return (self.is_traversal_valid_for('north', color, position) or
                self.is_traversal_valid_for('north_east', color, position) or
                self.is_traversal_valid_for('east', color, position) or
                self.is_traversal_valid_for('south_east', color, position) or
                self.is_traversal_valid_for('south', color, position) or
                self.is_traversal_valid_for('south_west', color, position) or
                self.is_traversal_valid_for('west', color, position) or
                self.is_traversal_valid_for('north_west', color, position))

    def flip_pieces(self, direction, color, position):
        next_column_index = ord(position[0]) - 65
        next_row_index = int(position[1]) - 1

        next_column_index += self.traversal_increments[direction]['column_increment']
        next_row_index += self.traversal_increments[direction]['row_increment']

        while self.piece_at(next_column_index, next_row_index) != color:
            self.board[chr(next_column_index + 65)][next_row_index + 1] = color

            next_column_index += self.traversal_increments[direction]['column_increment']
            next_row_index += self.traversal_increments[direction]['row_increment']

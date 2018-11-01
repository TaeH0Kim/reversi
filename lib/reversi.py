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
        board = {
            'A': {}, 'B': {}, 'C': {}, 'D': {},
            'E': {}, 'F': {}, 'G': {}, 'H': {}
            }
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
                'north-east': {'row_increment': -1, 'column_increment':  1},
                'north-west': {'row_increment': -1, 'column_increment': -1},
                'south-west': {'row_increment':  1, 'column_increment': -1},
                'south-east': {'row_increment':  1, 'column_increment':  1},
            }

    def move(self, position):
        column = position[0]
        row = int(position[1])

        self.board[column][row] = self.player

        if self.player == 'b':
            self.player = 'w'
        else:
            self.player = 'b'

        return True

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
                direction == 'north-east' and (col >= 7 or row <= 0)  or
                direction == 'north-west' and (col <= 0 or row <= 0)  or
                direction == 'south-east' and (col >= 7 or row >= 7))

    def does_east_traversal_allow_valid_move(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while self.continue_east(column_index, row_index):
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

    def does_west_traversal_allow_valid_move(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while self.continue_west(column_index, row_index):
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

    def does_north_traversal_allow_valid_move(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index  = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while self.continue_north(column_index, row_index):
            column_index += self.traversal_increments[direction]['column_increment']
            row_index += self.traversal_increments[direction]['row_increment']

            if color == self.piece_at(column_index, row_index) or self.piece_at(column_index, row_index) == '-':
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if color == self.piece_at(column_index, row_index) and opposite_color_count >= 1:
            return True

        return False

    def does_south_traversal_allow_valid_move(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while self.continue_south(column_index, row_index):
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

    def does_north_east_traversal_allow_valid_move(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while self.continue_north_east(column_index, row_index):
            column_index += self.traversal_increments[direction]['column_increment']
            row_index += self.traversal_increments[direction]['row_increment']

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if (color == self.piece_at(column_index, row_index) and
                opposite_color_count >= 1):
            return True

        return False

    def does_north_west_traversal_allow_valid_move(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while self.continue_north_west(column_index, row_index):
            column_index += self.traversal_increments[direction]['column_increment']
            row_index += self.traversal_increments[direction]['row_increment']

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if (color == self.piece_at(column_index, row_index) and
                opposite_color_count >= 1):
            return True

        return False

    def does_south_west_traversal_allow_valid_move(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while self.continue_south_west(column_index, row_index):
            column_index += self.traversal_increments[direction]['column_increment']
            row_index += self.traversal_increments[direction]['row_increment']

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if (color == self.piece_at(column_index, row_index) and
                opposite_color_count >= 1):
            return True

        return False

    def does_south_east_traversal_allow_valid_move(self, direction, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if self.too_close_to_edge(direction, column_index, row_index):
            return False

        opposite_color_count = 0
        while self.continue_south_east(column_index, row_index):
            column_index += self.traversal_increments[direction]['column_increment']
            row_index += self.traversal_increments[direction]['row_increment']

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if (color == self.piece_at(column_index, row_index) and
                opposite_color_count >= 1):
            return True

        return False

    def is_move_valid(self, color, position):
        if self.board[position[0]][int(position[1])] != '-':
            return False

        return (self.does_north_traversal_allow_valid_move('north', color, position) or
                self.does_north_east_traversal_allow_valid_move('north-east', color, position) or
                self.does_east_traversal_allow_valid_move('east', color, position) or
                self.does_south_east_traversal_allow_valid_move('south-east', color, position) or
                self.does_south_traversal_allow_valid_move('south', color, position) or
                self.does_south_west_traversal_allow_valid_move('south-west', color, position) or
                self.does_west_traversal_allow_valid_move('west', color, position) or
                self.does_north_west_traversal_allow_valid_move('north-west', color, position))

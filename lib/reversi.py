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

    def does_east_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if column_index >= 7:
            return False

        opposite_color_count = 0
        while column_index < 8:
            column_index += 1

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1
        if color == self.piece_at(column_index, row_index) and opposite_color_count >= 1:
            return True

        return False

    def does_west_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if column_index <= 0:
            return False

        opposite_color_count = 0
        while column_index > -1:
            column_index -= 1

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if color == self.piece_at(column_index, row_index) and opposite_color_count >= 1:
            return True

        return False

    def does_north_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index  = int(position[1]) - 1

        if row_index <= 1:
            return False

        opposite_color_count = 0
        while row_index > 0:
            row_index -= 1

            if color == self.piece_at(column_index, row_index) or self.piece_at(column_index, row_index) == '-':
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if color == self.piece_at(column_index, row_index) and opposite_color_count >= 1:
            return True

        return False

    def does_south_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if row_index >= 7:
            return False

        opposite_color_count = 0
        while row_index < 9:
            row_index += 1

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if color == self.piece_at(column_index, row_index) and opposite_color_count >= 1:
            return True

        return False

    def does_north_east_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if column_index >= 7 or row_index <= 0:
            return False

        opposite_color_count = 0
        while column_index < 7 and row_index > 0:
            row_index -= 1
            column_index += 1

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if (color == self.piece_at(column_index, row_index) and
                opposite_color_count >= 1):
            return True

        return False

    def does_north_west_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if column_index <= 0 or row_index <= 0:
            return False

        opposite_color_count = 0
        while column_index > 0 and row_index > 0:
            row_index -= 1
            column_index -= 1

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if (color == self.piece_at(column_index, row_index) and
                opposite_color_count >= 1):
            return True

        return False

    def does_south_west_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if column_index <= 0 or row_index >= 7:
            return False

        opposite_color_count = 0
        while column_index > 0 and row_index < 7:
            row_index += 1
            column_index -= 1

            if (color == self.piece_at(column_index, row_index) or
                    self.piece_at(column_index, row_index) == '-'):
                break
            elif self.piece_at(column_index, row_index) != '-':
                opposite_color_count += 1

        if (color == self.piece_at(column_index, row_index) and
                opposite_color_count >= 1):
            return True

        return False

    def does_south_east_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if column_index >= 7 or row_index >= 7:
            return False

        opposite_color_count = 0
        while column_index < 7 and row_index < 7:
            row_index += 1
            column_index += 1

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

        return (self.does_north_traversal_allow_valid_move(color, position) or
                self.does_north_east_traversal_allow_valid_move(color, position) or
                self.does_east_traversal_allow_valid_move(color, position) or
                self.does_south_east_traversal_allow_valid_move(color, position) or
                self.does_south_traversal_allow_valid_move(color, position) or
                self.does_south_west_traversal_allow_valid_move(color, position) or
                self.does_west_traversal_allow_valid_move(color, position) or
                self.does_north_west_traversal_allow_valid_move(color, position))

import unittest


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

    def does_east_traversal_allow_valid_move(self, color, position):
        column = position[0]
        column_index = ord(column) - 65
        row = int(position[1])

        if column_index >= 7:
            return False

        opposite_color_count = 0
        for i in range(column_index+1, 8):
            if (color == self.board[chr(i + 65)][row] or
                    self.board[chr(i + 65)][row] == '-'):
                break
            elif self.board[chr(i + 65)][row] != '-':
                opposite_color_count += 1
        if color == self.board[chr(i + 65)][row] and opposite_color_count >= 1:
            return True

        return False

    def does_west_traversal_allow_valid_move(self, color, position):
        column = position[0]
        column_index = ord(column) - 65
        row = int(position[1])

        if column_index <= 0:
            return False

        opposite_color_count = 0
        for i in range(column_index-1, -1, -1):
            if (color == self.board[chr(i + 65)][row] or
                    self.board[chr(i + 65)][row] == '-'):
                break
            elif self.board[chr(i + 65)][row] != '-':
                opposite_color_count += 1

        if color == self.board[chr(i + 65)][row] and opposite_color_count >= 1:
            return True

        return False

    def does_north_traversal_allow_valid_move(self, color, position):
        column = position[0]
        row = int(position[1])

        if row <= 1:
            return False

        opposite_color_count = 0
        for i in range(row-1, 0, -1):
            if color == self.board[column][i] or self.board[column][i] == '-':
                break
            elif self.board[column][i] != '-':
                opposite_color_count += 1

        if color == self.board[column][i] and opposite_color_count >= 1:
            return True

        return False

    def does_south_traversal_allow_valid_move(self, color, position):
        column = position[0]
        row = int(position[1])

        if row >= 8:
            return False

        opposite_color_count = 0
        for i in range(row+1, 9):
            if (color == self.board[column][i] or
                    self.board[column][i] == '-'):
                break
            elif self.board[column][i] != '-':
                opposite_color_count += 1

        if color == self.board[column][i] and opposite_color_count >= 1:
            return True

        return False

    def does_north_east_traversal_allow_valid_move(self, color, position):
        column = position[0]
        column_index = ord(column) - 65
        row_index = int(position[1]) - 1

        if column_index >= 7 or row_index <= 0:
            return False

        column_position = column_index
        row_position = row_index
        opposite_color_count = 0
        while column_position < 7 and row_position > 0:
            row_position -= 1
            column_position += 1

            if (color == self.board[chr(column_position + 65)][row_position+1] or
                    self.board[chr(column_position + 65)][row_position+1] == '-'):
                break
            elif self.board[chr(column_position + 65)][row_position+1] != '-':
                opposite_color_count += 1

        if (color == self.board[chr(column_position + 65)][row_position+1] and
                opposite_color_count >= 1):
            return True

        return False

    def does_north_west_traversal_allow_valid_move(self, color, position):
        column = position[0]
        column_index = ord(column) - 65
        row_index = int(position[1]) - 1

        if column_index <= 0 or row_index <= 0:
            return False

        column_position = column_index
        row_position = row_index
        opposite_color_count = 0
        while column_position > 0 and row_position > 0:
            row_position -= 1
            column_position -= 1

            if (color == self.board[chr(column_position + 65)][row_position+1] or
                    self.board[chr(column_position + 65)][row_position+1] == '-'):
                break
            elif self.board[chr(column_position + 65)][row_position+1] != '-':
                opposite_color_count += 1

        if (color == self.board[chr(column_position + 65)][row_position+1] and
                opposite_color_count >= 1):
            return True

        return False

    def does_south_west_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if column_index <= 0 or row_index >= 7:
            return False

        column_position = column_index
        row_position = row_index
        opposite_color_count = 0
        while column_position > 0 and row_position < 7:
            row_position += 1
            column_position -= 1

            if (color == self.board[chr(column_position + 65)][row_position+1] or
                    self.board[chr(column_position + 65)][row_position+1] == '-'):
                break
            elif self.board[chr(column_position + 65)][row_position+1] != '-':
                opposite_color_count += 1

        if (color == self.board[chr(column_position + 65)][row_position+1] and
                opposite_color_count >= 1):
            return True

        return False

    def does_south_east_traversal_allow_valid_move(self, color, position):
        column_index = ord(position[0]) - 65
        row_index = int(position[1]) - 1

        if column_index >= 7 or row_index >= 7:
            return False

        column_position = column_index
        row_position = row_index
        opposite_color_count = 0
        while column_position < 7 and row_position < 7:
            row_position += 1
            column_position += 1

            if (color == self.board[chr(column_position + 65)][row_position+1] or
                    self.board[chr(column_position + 65)][row_position+1] == '-'):
                break
            elif self.board[chr(column_position + 65)][row_position+1] != '-':
                opposite_color_count += 1

        if (color == self.board[chr(column_position + 65)][row_position+1] and
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


class TestReversi(unittest.TestCase):

    def test_move_changes_player(self):
        r = Reversi()
        self.assertEqual(r.player, 'b')
        r.move("A1")
        self.assertEqual(r.player, 'w')
        r.move("A2")
        self.assertEqual(r.player, 'b')

    def test_move_places_piece_on_board(self):
        r = Reversi()
        r.move('A1')
        self.assertEqual(r.board['A'][1], 'b')
        r.move('B7')
        self.assertEqual(r.board['B'][7], 'w')

    def test_does_east_traversal_allow_valid_move(self):
        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - b - - - -
            - - - b b - - -
            - - w w b - - -
            - - - - b - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.does_east_traversal_allow_valid_move('b', 'B5'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - b - - - -
            - - - b b - - -
            - - - w b - - -
            - - - - b - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.does_east_traversal_allow_valid_move('b', 'C5'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - b - - - -
            - - - b b - - -
            - - w w w - - -
            - - - - b - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_east_traversal_allow_valid_move('b', 'B5'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - b - - - -
            - - - b b - - -
            - - w w w - - -
            - - - - b - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_east_traversal_allow_valid_move('b', 'H2'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_east_traversal = {'C4'}
        moves_invalid_for_east_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'} - moves_valid_for_east_traversal

        for move in moves_valid_for_east_traversal:
            self.assertTrue(r.does_east_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        for move in moves_invalid_for_east_traversal:
            self.assertFalse(r.does_east_traversal_allow_valid_move('b', move),
            "error for position: " + move)

    def test_does_west_traversal_allow_valid_move(self):
        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_west_traversal = {'F5'}
        moves_invalid_for_west_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'} - moves_valid_for_west_traversal

        for move in moves_valid_for_west_traversal:
            self.assertTrue(r.does_west_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        for move in moves_invalid_for_west_traversal:
            self.assertFalse(r.does_west_traversal_allow_valid_move('b', move),
            "error for position: " + move)

    def test_does_north_traversal_allow_valid_move(self):

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_north_traversal = {'E6'}
        moves_invalid_for_north_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'} - moves_valid_for_north_traversal

        for move in moves_valid_for_north_traversal:
            self.assertTrue(r.does_north_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        for move in moves_invalid_for_north_traversal:
            self.assertFalse(r.does_north_traversal_allow_valid_move('b', move),
            "error for position: " + move)

    def test_does_south_traversal_allow_valid_move(self):

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_south_traversal = {'D3'}
        moves_invalid_for_south_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'} - moves_valid_for_south_traversal

        for move in moves_valid_for_south_traversal:
            self.assertTrue(r.does_south_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        for move in moves_invalid_for_south_traversal:
            self.assertFalse(r.does_south_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        r = Reversi('''
            - - - - - - - -
            - - - w - - - -
            - - w w w - - -
            - - - w w - - -
            - - - w w - - -
            - - - w b b b -
            - - - w b - - -
            - - - b - - - -
            ''')
        self.assertTrue(r.does_south_traversal_allow_valid_move('b', 'D1'))

    def test_does_north_east_traversal_allow_valid_move(self):

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_invalid_for_north_east_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'}

        for move in moves_invalid_for_north_east_traversal:
            self.assertFalse(r.does_north_east_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        r = Reversi('''
            - - - - - - - -
            - - - w - - - -
            - - w w w w - -
            - b b w w b - -
            - - w w w - - -
            - b w - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_north_east_traversal = {'D6'}
        moves_invalid_for_north_east_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'} - moves_valid_for_north_east_traversal

        for move in moves_valid_for_north_east_traversal:
            self.assertTrue(r.does_north_east_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        for move in moves_invalid_for_north_east_traversal:
            self.assertFalse(r.does_north_east_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - w b b - -
            - - - w - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.does_north_east_traversal_allow_valid_move('b', 'C7'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - b b b b - -
            - - - w - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_north_east_traversal_allow_valid_move('b', 'C6'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - b b b b - -
            - - - w - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_north_east_traversal_allow_valid_move('b', 'A7'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - w w w w -
            - - - b - - - -
            - - b - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.does_north_east_traversal_allow_valid_move('w', 'B8'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_north_east_traversal_allow_valid_move('w', 'A6'))

    def test_does_north_west_traversal_allow_valid_move(self):
        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_invalid_for_north_west_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'}

        for move in moves_invalid_for_north_west_traversal:
            self.assertFalse(r.does_north_west_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - b b b - - -
            - - - b b - - -
            - - - w w w - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_north_west_traversal = {'F7', 'G7'}
        moves_invalid_for_north_west_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'} - moves_valid_for_north_west_traversal

        for move in moves_valid_for_north_west_traversal:
            self.assertTrue(r.does_north_west_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        for move in moves_invalid_for_north_west_traversal:
            self.assertFalse(r.does_north_west_traversal_allow_valid_move('b', move),
            "error for position: " + move)

    def test_does_south_west_traversal_allow_valid_move(self):
        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_invalid_for_south_west_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'}
        for move in moves_invalid_for_south_west_traversal:
            self.assertFalse(r.does_south_west_traversal_allow_valid_move('b', move),
            "error for position: " + move)
        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w w w - -
            - - - w b b - -
            - - - b - - - -
            - - b - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_south_west_traversal = {'G3'}
        moves_invalid_for_south_west_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'} - moves_valid_for_south_west_traversal
        for move in moves_valid_for_south_west_traversal:
            self.assertTrue(r.does_south_west_traversal_allow_valid_move('b', move),
            "error for position: " + move)
        for move in moves_invalid_for_south_west_traversal:
            self.assertFalse(r.does_south_west_traversal_allow_valid_move('b', move),
            "error for position: " + move)

    def test_does_south_east_traversal_allow_valid_move(self):
        r = Reversi('''
            - - - - - - - -
            - - b w - - - -
            - - b w b - - -
            - - b w b - - -
            - w b w w w w -
            w w b b b - - -
            - - b b - - - -
            - - - b - - - -
            ''')
        self.assertTrue(r.does_south_east_traversal_allow_valid_move('b', 'A4'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_invalid_for_south_east_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'}

        for move in moves_invalid_for_south_east_traversal:
            self.assertFalse(r.does_south_east_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w w w - -
            - - - w b b - -
            - - - b - - - -
            - - b - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_south_east_traversal = {'C3', 'D3'}
        moves_invalid_for_south_east_traversal = {'A1', 'A2', 'A3', 'A4', 'A5',
            'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3',
            'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1',
            'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
            'H5', 'H6', 'H7', 'H8'} - moves_valid_for_south_east_traversal

        for move in moves_valid_for_south_east_traversal:
            self.assertTrue(r.does_south_east_traversal_allow_valid_move('b', move),
            "error for position: " + move)

        for move in moves_invalid_for_south_east_traversal:
            self.assertFalse(r.does_south_east_traversal_allow_valid_move('b', move),
            "error for position: " + move)

    def test_is_move_valid(self):
        r = Reversi('''
            - - - - - - - -
            - - b w - - - -
            - - b w b - - -
            - - b w b - - -
            - w b w w w w -
            w w b b b - - -
            - - b b - - - -
            - - - b - - - -
            ''')

        valid_moves = {'A4', 'A5', 'A7', 'C1', 'D1', 'E1', 'E2', 'F4', 'F6',
            'G4', 'G6', 'H5'}
        invalid_moves = {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1',
            'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4',
            'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
            'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2',
            'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5',
            'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'
            } - valid_moves

        self.assertTrue(r.is_move_valid('b', 'A4'))
        for move in valid_moves:
            self.assertTrue(r.is_move_valid('b', move),
            "error for position: " + move)

        for move in invalid_moves:
            self.assertFalse(r.is_move_valid('b', move),
            "error for position: " + move)

        r = Reversi('''
            - - - - - - - -
            - - - b w - w -
            - - w b w b b -
            - - - b w - - -
            - - - b w b - -
            - - - - w - - -
            - - - - - - - -
            - - - - - - - -
            ''')

        valid_moves = {'B2', 'B3', 'B4', 'D1', 'D7', 'F1', 'F2', 'F4', 'F6',
            'F7', 'G1', 'H1'}
        invalid_moves = {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1',
            'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4',
            'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
            'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2',
            'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5',
            'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'
            } - valid_moves

        for move in valid_moves:
            self.assertTrue(r.is_move_valid('b', move),
            "error for position: " + move)

        for move in invalid_moves:
            self.assertFalse(r.is_move_valid('b', move),
            "error for position: " + move)

        r = Reversi('''
            - - - - - w - -
            - - b - w - - -
            - - b b b - - -
            - - b w b w - -
            - - b w b w w -
            - - b w b b - -
            - - - b b - - -
            - - - b b - - -
            ''')

        valid_moves = {'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C8', 'D2',
            'F2', 'F3', 'F7', 'F8', 'G6', 'G7'}
        invalid_moves = {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1',
            'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4',
            'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
            'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2',
            'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5',
            'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'
            } - valid_moves

        for move in valid_moves:
            self.assertTrue(r.is_move_valid('w', move),
            "error for position: " + move)

        for move in invalid_moves:
            self.assertFalse(r.is_move_valid('w', move),
            "error for position: " + move)

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - w - w - - -
            - - w w w w - -
            - - w b b b b b
            - - - b b w - -
            - - - w b - - -
            - - w - b - - -
            ''')

        valid_moves = {'C6', 'C7', 'D8', 'F7', 'F8', 'G4', 'G6', 'H4', 'H6'}
        invalid_moves = {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1',
            'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4',
            'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
            'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2',
            'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5',
            'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'
            } - valid_moves

        for move in valid_moves:
            self.assertTrue(r.is_move_valid('w', move),
            "error for position: " + move)

        for move in invalid_moves:
            self.assertFalse(r.is_move_valid('w', move),
            "error for position: " + move)

if __name__ == '__main__':
    unittest.main()
